#!/usr/bin/env python3
# Minimal XOR MLP from scratch (NumPy only)

import argparse
import time
from dataclasses import dataclass

import numpy as np

np.set_printoptions(precision=4, suppress=True)


def xavier_init(f_in, f_out, rng):
    """Xavier/Glorot uniform initializer."""
    limit = np.sqrt(6.0 / (f_in + f_out))
    return rng.uniform(-limit, limit, size=(f_in, f_out)).astype(np.float64)


@dataclass
class MLP:
    """Tiny 2->H->1 MLP with ReLU hidden and sigmoid output.

    Uses SGD with momentum. Designed for the XOR task.
    """
    in_dim: int
    hidden: int
    out_dim: int
    seed: int = 42
    momentum: float = 0.9

    def __post_init__(self):
        self.rng = np.random.default_rng(self.seed)
        # Parameters
        self.W1 = xavier_init(self.in_dim, self.hidden, self.rng)
        self.b1 = np.zeros((1, self.hidden), dtype=np.float64)
        self.W2 = xavier_init(self.hidden, self.out_dim, self.rng)
        self.b2 = np.zeros((1, self.out_dim), dtype=np.float64)
        # Velocity buffers for SGD + momentum
        self.vW1 = np.zeros_like(self.W1)
        self.vb1 = np.zeros_like(self.b1)
        self.vW2 = np.zeros_like(self.W2)
        self.vb2 = np.zeros_like(self.b2)

    # Activations
    @staticmethod
    def relu(z):
        return np.maximum(0.0, z)

    @staticmethod
    def relu_grad(z):
        return (z > 0.0).astype(np.float64)

    @staticmethod
    def sigmoid(z):
        # Stable-ish sigmoid for small net; for very large |z|, np.exp over/underflow is possible.
        return 1.0 / (1.0 + np.exp(-z))

    def forward(self, X):
        """Compute forward pass and return (y_hat, cache)."""
        z1 = X @ self.W1 + self.b1
        h1 = self.relu(z1)
        z2 = h1 @ self.W2 + self.b2
        y_hat = self.sigmoid(z2)
        cache = (X, z1, h1, z2, y_hat)
        return y_hat, cache

    @staticmethod
    def bce_loss(y_hat, y_true, eps=1e-9):
        """Binary cross-entropy loss. Clipped to avoid log(0)."""
        y_hat = np.clip(y_hat, eps, 1 - eps)
        return float(-np.mean(y_true * np.log(y_hat) + (1 - y_true) * np.log(1 - y_hat)))

    def step(self, grads, lr):
        """SGD with momentum parameter update."""
        dW1, db1, dW2, db2 = grads
        self.vW1 = self.momentum * self.vW1 - lr * dW1
        self.vb1 = self.momentum * self.vb1 - lr * db1
        self.vW2 = self.momentum * self.vW2 - lr * dW2
        self.vb2 = self.momentum * self.vb2 - lr * db2
        self.W1 += self.vW1
        self.b1 += self.vb1
        self.W2 += self.vW2
        self.b2 += self.vb2

    def backward(self, cache, y_true):
        """Backprop through sigmoid + BCE and ReLU layer.

        For BCE with sigmoid output, dL/dz2 simplifies to (y_hat - y_true).
        """
        X, z1, h1, _z2, y_hat = cache
        m = X.shape[0]
        dz2 = (y_hat - y_true) / m  # (4,1)
        dW2 = h1.T @ dz2            # (H,1)
        db2 = np.sum(dz2, axis=0, keepdims=True)
        dh1 = dz2 @ self.W2.T       # (4,H)
        dz1 = dh1 * self.relu_grad(z1)
        dW1 = X.T @ dz1
        db1 = np.sum(dz1, axis=0, keepdims=True)
        return dW1, db1, dW2, db2

    def predict(self, X):
        """Return binary predictions in {0,1}."""
        y_hat, _ = self.forward(X)
        return (y_hat >= 0.5).astype(np.int32)


def xor_data():
    """Hard-coded XOR dataset: 4 points in R^2 with labels in {0,1}."""
    X = np.array(
        [[0.0, 0.0],
         [0.0, 1.0],
         [1.0, 0.0],
         [1.0, 1.0]],
        dtype=np.float64,
    )
    y = np.array([[0.0], [1.0], [1.0], [0.0]], dtype=np.float64)
    return X, y


def train(epochs=3000, lr=0.1, hidden=8, seed=7, log_every=300):
    """Train on XOR with full-batch updates. Returns (model, accuracy, elapsed_sec).

    Guardrail: if loss becomes NaN or increases monotonically for a while,
    we fall back once to safer hyperparameters (lower lr, different seed).
    """
    X, y = xor_data()

    def run(epochs, lr, seed, log_every):
        model = MLP(2, hidden, 1, seed=seed)
        last_losses = []
        t0 = time.perf_counter()
        for ep in range(1, epochs + 1):
            y_hat, cache = model.forward(X)
            loss = model.bce_loss(y_hat, y)
            grads = model.backward(cache, y)
            model.step(grads, lr)

            # Track recent losses to detect divergence/instability.
            last_losses.append(loss)
            if len(last_losses) > 20:
                last_losses.pop(0)

            if ep % log_every == 0 or ep == 1 or ep == epochs:
                preds = model.predict(X)
                acc = float((preds == y).mean())
                print(f"epoch {ep:4d} | loss {loss:.6f} | acc {acc:.3f}")

        elapsed = time.perf_counter() - t0
        preds = model.predict(X)
        acc = float((preds == y).mean())
        return model, acc, elapsed, last_losses

    model, acc, elapsed, last_losses = run(epochs, lr, seed, log_every)

    # Simple divergence heuristic: NaN loss or strictly increasing recent loss.
    def is_diverging(losses):
        if any(not np.isfinite(l) for l in losses):
            return True
        if len(losses) >= 6 and all(losses[i] < losses[i + 1] for i in range(len(losses) - 1)):
            return True
        return False

    if is_diverging(last_losses):
        print("Detected potential divergence/instability. Falling back to safer hyperparams "
              "(lr=0.05, seed=seed+1).")
        model, acc, elapsed, _ = run(epochs, 0.05, seed + 1, log_every)

    return model, acc, elapsed


def main():
    parser = argparse.ArgumentParser(description="Minimal XOR MLP (NumPy only)")
    parser.add_argument("--epochs", type=int, default=3000, help="Training epochs (default: 3000)")
    parser.add_argument("--lr", type=float, default=0.1, help="Learning rate (default: 0.1)")
    parser.add_argument("--hidden", type=int, default=8, help="Hidden units (default: 8)")
    parser.add_argument("--seed", type=int, default=7, help="PRNG seed for determinism (default: 7)")
    parser.add_argument("--test", action="store_true", help="Run smoke test and exit")
    args = parser.parse_args()

    if args.test:
        # Smoke test: require near-perfect accuracy on XOR quickly.
        _, acc, elapsed = train(epochs=2000, lr=0.1, hidden=args.hidden, seed=args.seed, log_every=1000)
        assert acc >= 0.99, f"Accuracy too low: {acc:.3f}"
        print("Smoke test passed.")
        # Print elapsed to help verify <2s on typical laptop CPUs.
        print(f"Elapsed seconds (test run): {elapsed:.4f}")
        return

    _, acc, elapsed = train(epochs=args.epochs, lr=args.lr, hidden=args.hidden, seed=args.seed)
    print(f"Final accuracy: {acc:.3f}")
    print(f"Elapsed seconds: {elapsed:.4f}")


if __name__ == "__main__":
    main()

import random
from engine import Value


class ZeroGrad:
    def zero_grad(self):
        for p in self.parameters():
            p.grad = 0

    def parameters(self):
        return []


class Neuron(ZeroGrad):
    def __init__(self, nin: int):
        self.w = [Value(random.uniform(-1, 1)) for _ in range(0, nin)]
        self.b = Value(random.uniform(-1, 1))

    def __call__(self, x: float | int):
        act = sum((wi * xi for wi, xi in zip(self.w, x)), self.b)
        out = act.tanh()
        return out

    def __repr__(self):
        return f"{[cell.data for cell in self.w]}\n"

    def parameters(self):
        return self.w + [self.b]


class Layer(ZeroGrad):
    def __init__(self, nin: int, nout: int):
        self.neurons = [Neuron(nin) for _ in range(nout)]
        self.b = Value(random.uniform(-1, 1))

    def __call__(self, x):
        outs = [n(x) for n in self.neurons]
        return outs[0] if len(outs) == 1 else outs

    def __repr__(self):
        return f"Layer of [\n{''.join(str(n) for n in self.neurons)}]"

    def parameters(self):
        return [p for neuron in self.neurons for p in neuron.parameters()]


class MLP(ZeroGrad):
    def __init__(self, nin: int, nouts: list):
        sz = [nin] + nouts
        self.layers = [Layer(sz[i], sz[i + 1]) for i in range(len(nouts))]

    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

    def __repr__(self):
        return f"MLP of [{', '.join(str(layer) for layer in self.layers)}]"

    def parameters(self):
        return [p for layer in self.layers for p in layer.parameters()]

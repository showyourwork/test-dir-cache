import matplotlib.pyplot as plt
import numpy as np
import paths
np.random.seed(0)
data = np.array([np.load(paths.data / 'test_data' / f'test_data{n:02d}.npz')['data'] for n in range(50)])
fig = plt.figure(figsize=(7, 6))
plt.plot(data)
fig.savefig(paths.figures / 'test_figure.pdf', bbox_inches='tight', dpi=300)

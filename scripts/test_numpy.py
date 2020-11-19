import numpy as np
def test_numpy():
	a = np.array([[0, 1, 2],
              [0, -2, 4],
              [0, 3, -6]])
	print(a>0.0)
	b = np.where(a>=0,  a, -a)
	print(b)
	print(np.logical_or((a>0.0), (a<0.0)))

if __name__ == "__main__":
	# simulate_consistent()
	# compute_L_pre()
	test_numpy()
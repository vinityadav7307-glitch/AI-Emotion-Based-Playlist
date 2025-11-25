"""
Principal Component Analysis (PCA) on Iris Dataset
B.Tech AIML - Linear Algebra Project
Minimal Version - No Pandas Required
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

print("="*60)
print("PCA PROJECT - IRIS DATASET")
print("="*60)

# ============================================================
# STEP 1: LOAD DATASET
# ============================================================
print("\n[STEP 1] Loading Iris Dataset...")
iris = load_iris()
X = iris.data              # 150 samples x 4 features
y = iris.target            # class labels (0, 1, 2)
feature_names = iris.feature_names
target_names = iris.target_names

print(f"Dataset Shape: {X.shape}")
print(f"Features: {feature_names}")
print(f"Classes: {target_names}")
print(f"\nFirst 5 samples:")
for i in range(5):
    print(f"  {X[i]}")

# ============================================================
# STEP 2: STANDARDIZE DATA
# ============================================================
print("\n[STEP 2] Standardizing Data...")
scaler = StandardScaler()
X_standardized = scaler.fit_transform(X)

print(f"Original Mean: {X.mean(axis=0)}")
print(f"Standardized Mean: {X_standardized.mean(axis=0)}")
print(f"Standardized Std: {X_standardized.std(axis=0)}")

# ============================================================
# STEP 3: COMPUTE COVARIANCE MATRIX
# ============================================================
print("\n[STEP 3] Computing Covariance Matrix...")
cov_matrix = np.cov(X_standardized.T)
print(f"Covariance Matrix Shape: {cov_matrix.shape}")
print(f"Covariance Matrix:")
print(cov_matrix)

# ============================================================
# STEP 4: CALCULATE EIGENVALUES & EIGENVECTORS
# ============================================================
print("\n[STEP 4] Calculating Eigenvalues and Eigenvectors...")
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

print(f"\nEigenvalues: {eigenvalues}")
print(f"\nEigenvectors (columns are eigenvectors):")
print(eigenvectors)

# ============================================================
# STEP 5: SORT BY EIGENVALUES (DESCENDING)
# ============================================================
print("\n[STEP 5] Sorting by Eigenvalues...")
# Create list of (eigenvalue, eigenvector) pairs
eigen_pairs = [(eigenvalues[i], eigenvectors[:, i])
               for i in range(len(eigenvalues))]

# Sort in descending order
eigen_pairs.sort(key=lambda x: x[0], reverse=True)

print("\nSorted Eigenvalues:")
for i, pair in enumerate(eigen_pairs):
    print(f"  PC{i+1}: λ = {pair[0]:.4f}")

# ============================================================
# STEP 6: CALCULATE EXPLAINED VARIANCE
# ============================================================
print("\n[STEP 6] Calculating Explained Variance...")
total_variance = sum(eigenvalues)
explained_variance = [(ev / total_variance) * 100
                      for ev in eigenvalues]
cumulative_variance = np.cumsum(explained_variance)

print("\nExplained Variance Ratio:")
for i, var in enumerate(explained_variance):
    print(f"  PC{i+1}: {var:.2f}%")

print(f"\nCumulative Variance (PC1 + PC2): {cumulative_variance[1]:.2f}%")

# ============================================================
# STEP 7: CREATE PROJECTION MATRIX (SELECT TOP 2 PCs)
# ============================================================
print("\n[STEP 7] Creating Projection Matrix...")
# Select top 2 principal components
W = np.column_stack([eigen_pairs[0][1], eigen_pairs[1][1]])
print(f"Projection Matrix W shape: {W.shape}")
print(f"W (first 2 eigenvectors as columns):")
print(W)

# ============================================================
# STEP 8: TRANSFORM DATA TO 2D
# ============================================================
print("\n[STEP 8] Transforming Data...")
X_pca = X_standardized.dot(W)
print(f"Transformed Data Shape: {X_pca.shape}")
print(f"Original: {X.shape} -> PCA: {X_pca.shape}")
print(f"Dimensionality Reduction: {(1 - X_pca.shape[1]/X.shape[1])*100:.0f}%")

# ============================================================
# STEP 9: VERIFICATION
# ============================================================
print("\n[STEP 9] Verification...")
# Verify: Cov(X) × v = λ × v
v1 = eigen_pairs[0][1]
lambda1 = eigen_pairs[0][0]

left_side = cov_matrix.dot(v1)
right_side = lambda1 * v1

print("Verifying Eigenvalue Equation: Cov(X) × v = λ × v")
print(f"Are they equal? {np.allclose(left_side, right_side)}")

# Verify orthogonality
pc1 = eigen_pairs[0][1]
pc2 = eigen_pairs[1][1]
dot_product = np.dot(pc1, pc2)
print(f"\nVerifying Orthogonality: PC1 · PC2 = {dot_product:.10f}")
print(f"Are they orthogonal? {np.isclose(dot_product, 0)}")

# ============================================================
# STEP 10: VISUALIZATION
# ============================================================
print("\n[STEP 10] Creating Visualizations...")

# Setup colors
colors = ['red', 'green', 'blue']

# Create figure with 2 subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Original Data (first 2 features only)
ax1 = axes[0]
for i, target_name in enumerate(target_names):
    mask = y == i
    ax1.scatter(X[mask, 0], X[mask, 1],
                color=colors[i], label=target_name,
                alpha=0.7, edgecolors='black', s=60)
ax1.set_xlabel(feature_names[0], fontsize=12, fontweight='bold')
ax1.set_ylabel(feature_names[1], fontsize=12, fontweight='bold')
ax1.set_title('Original Data (First 2 Features Only)', fontsize=14, fontweight='bold')
ax1.legend(loc='best', fontsize=10)
ax1.grid(True, alpha=0.3)

# Plot 2: PCA Transformed Data
ax2 = axes[1]
for i, target_name in enumerate(target_names):
    mask = y == i
    ax2.scatter(X_pca[mask, 0], X_pca[mask, 1],
                color=colors[i], label=target_name,
                alpha=0.7, edgecolors='black', s=60)
ax2.set_xlabel(f'PC1 ({explained_variance[0]:.1f}% variance)',
               fontsize=12, fontweight='bold')
ax2.set_ylabel(f'PC2 ({explained_variance[1]:.1f}% variance)',
               fontsize=12, fontweight='bold')
ax2.set_title('PCA Transformed Data (All 4 Features)', fontsize=14, fontweight='bold')
ax2.legend(loc='best', fontsize=10)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('pca_comparison.png', dpi=300, bbox_inches='tight')
print("✓ Saved: pca_comparison.png")

# Create Scree Plot
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Explained Variance (Bar Chart)
ax1 = axes[0]
bars = ax1.bar(range(1, 5), explained_variance,
               alpha=0.8, color='steelblue', edgecolor='black')
ax1.set_xlabel('Principal Component', fontsize=12, fontweight='bold')
ax1.set_ylabel('Explained Variance (%)', fontsize=12, fontweight='bold')
ax1.set_title('Scree Plot - Individual Variance', fontsize=14, fontweight='bold')
ax1.set_xticks(range(1, 5))
ax1.set_xticklabels([f'PC{i}' for i in range(1, 5)])
ax1.grid(True, alpha=0.3, axis='y')

# Add value labels on bars
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
            f'{explained_variance[i]:.1f}%',
            ha='center', va='bottom', fontweight='bold')

# Plot 2: Cumulative Variance
ax2 = axes[1]
ax2.plot(range(1, 5), cumulative_variance,
         marker='o', linestyle='--', color='red',
         linewidth=2, markersize=10)
ax2.set_xlabel('Number of Components', fontsize=12, fontweight='bold')
ax2.set_ylabel('Cumulative Explained Variance (%)', fontsize=12, fontweight='bold')
ax2.set_title('Cumulative Variance Explained', fontsize=14, fontweight='bold')
ax2.set_xticks(range(1, 5))
ax2.grid(True, alpha=0.3)
ax2.axhline(y=95, color='green', linestyle=':', linewidth=2, label='95% threshold')
ax2.legend()

# Add value labels
for i in range(4):
    ax2.text(i+1, cumulative_variance[i] + 1,
            f'{cumulative_variance[i]:.1f}%',
            ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('variance_plots.png', dpi=300, bbox_inches='tight')
print("✓ Saved: variance_plots.png")

plt.show()

# ============================================================
# FINAL SUMMARY
# ============================================================
print("\n" + "="*60)
print("SUMMARY OF RESULTS")
print("="*60)
print(f"Original Dimensions:        4D")
print(f"Reduced Dimensions:         2D")
print(f"Information Preserved:      {cumulative_variance[1]:.2f}%")
print(f"Information Lost:           {100 - cumulative_variance[1]:.2f}%")
print(f"Dimensionality Reduction:   {(1 - 2/4)*100:.0f}%")
print(f"\nPC1 captures:               {explained_variance[0]:.2f}% variance")
print(f"PC2 captures:               {explained_variance[1]:.2f}% variance")
print(f"PC3 captures:               {explained_variance[2]:.2f}% variance")
print(f"PC4 captures:               {explained_variance[3]:.2f}% variance")
print("\n✓ PCA Analysis Complete!")
print("="*60)
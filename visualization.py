import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# Histogram ve dağılım grafikleri
def plot_distributions(data, columns):
    """
    Verilen sütunlar için histogram ve dağılım grafikleri çizer.
    - Parametreler:
        - data: Veri seti (DataFrame)
        - columns: Görselleştirilecek sütunların listesi
    """
    for column in columns:
        plt.figure(figsize=(8, 4))
        sns.histplot(data[column], kde=True)
        plt.title(f"{column} Dağılımı")
        plt.xlabel(column)
        plt.ylabel("Frekans")
        plt.show()

# Korelasyon matrisi
def plot_correlation_matrix(data):
    """
    Veri setinin korelasyon matrisini bir ısı haritası olarak çizer.
    - Parametreler:
        - data: Veri seti (DataFrame)
    """
    plt.figure(figsize=(10, 8))
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Korelasyon Matrisi")
    plt.show()

# 3D dağılım grafiği
def plot_3d_scatter(data, x, y, z, target=None):
    """
    3D dağılım grafiği çizer.
    - Parametreler:
        - data: Veri seti (DataFrame)
        - x, y, z: X, Y, Z eksenindeki sütun adları
        - target: Opsiyonel, renklendirme için bir hedef sütun
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    if target:
        scatter = ax.scatter(data[x], data[y], data[z], c=data[target], cmap="coolwarm")
        legend1 = ax.legend(*scatter.legend_elements(), title=target)
        ax.add_artist(legend1)
    else:
        ax.scatter(data[x], data[y], data[z], cmap="coolwarm")
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_zlabel(z)
    plt.title(f"3D Dağılım: {x}, {y}, {z}")
    plt.show()

# Kutu grafikleri (Boxplots)
def plot_boxplots(data, columns):
    """
    Verilen sütunlar için kutu grafikleri çizer.
    - Parametreler:
        - data: Veri seti (DataFrame)
        - columns: Görselleştirilecek sütunların listesi
    """
    for column in columns:
        plt.figure(figsize=(8, 4))
        sns.boxplot(data[column])
        plt.title(f"{column} Kutu Grafiği")
        plt.show()

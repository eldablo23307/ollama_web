pkgname=ollama-web-git
pkgver=r1.0000000
pkgrel=1
pkgdesc="Minimal Flask web interface for chatting with Ollama models"
arch=("any")
url="https://github.com/eldablo23307/ollama_web"
license=("MIT")
depends=("python" "python-flask" "python-pip")
makedepends=("git" "python-build" "python-installer" "python-setuptools" "python-wheel")
provides=("ollama-web")
conflicts=("ollama-web")
source=("git+https://github.com/eldablo23307/ollama_web.git")
sha256sums=("SKIP")

pkgver() {
  cd "$srcdir/ollama_web"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short=7 HEAD)"
}

build() {
  cd "$srcdir/ollama_web"
  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir/ollama_web"
  python -m installer --destdir="$pkgdir" dist/*.whl
  
  # Installa ollama da pip
  PIP_CONFIG_FILE=/dev/null pip install --isolated --root="$pkgdir" --ignore-installed --no-deps ollama
  
  # Installa la licenza
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
pkgname=ollama-web-git
pkgver=1.0.0.r0.g0000000
pkgrel=1
pkgdesc="Minimal Flask web interface for chatting with Ollama models"
arch=("any")
url="https://github.com/eldablo23307/ollama_web"
license=("MIT")
depends=("python" "python-flask" "python-ollama")
makedepends=("git" "python-build" "python-installer" "python-setuptools" "python-wheel")
provides=("ollama-web")
conflicts=("ollama-web")
source=("git+https://github.com/eldablo23307/ollama_web.git")
sha256sums=("SKIP")

pkgver() {
  cd "$srcdir/ollama_web"
  local version
  version=$(git describe --long --tags --abbrev=7 --match "v*" 2>/dev/null)
  if [[ -n "$version" ]]; then
    printf "%s" "${version#v}" | sed "s/-/.r/; s/-/./"
  else
    printf "0.r%s.g%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short=7 HEAD)"
  fi
}

build() {
  cd "$srcdir/ollama_web"
  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir/ollama_web"
  python -m installer --destdir="$pkgdir" dist/*.whl
  
  # Installa la licenza
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
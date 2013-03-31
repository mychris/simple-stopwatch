# Maintainer: mychris <just.mychris@googlemail.com>
pkgname=simple-stopwatch
pkgver=20130331
pkgrel=1
pkgdesc="A very simple python3, ncurses based terminal stopwatch."
arch=('any')
url="https://github.com/mychris/simple-stopwatch"
license=('GPL3 or any later version')
depends=('python')
makedepends=('git')
provides=('simple-stopwatch')
conflicts=()
replaces=()
backup=()
options=(!emptydirs)
source=()
md5sums=()

_gitroot=git://github.com/mychris/simple-stopwatch.git
_gitname=simple-stopwatch

pkgver() {
  cd "${srcdir}/${_gitname}"
  git describe --always | sed 's/-/_/g;s/v//'
}

package() {
  cd "$srcdir"
  msg "Connecting to GIT server...."

  if [[ -d "${_gitname}" ]]; then
    cd "${_gitname}" && git pull origin
    msg "The local files are updated."
  else
    git clone "${_gitroot}" "${_gitname}"
  fi

  msg "GIT checkout done or server timeout"
  msg "Starting build..."

  rm -rf "${srcdir}/${_gitname}-build"
  git clone "${srcdir}/${_gitname}" "${srcdir}/${_gitname}-build"
  cd "${srcdir}/${_gitname}-build"

  python3 setup.py install --root="${pkgdir}/" --optimize=1
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  python setup.py install --root="$pkgdir/" --optimize=1
}

# vim: ts=2 sw=2 et:
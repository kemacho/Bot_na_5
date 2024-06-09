{pkgs}: {
  deps = [
    pkgs.borgbackup
    pkgs.rustc
    pkgs.openssl
    pkgs.libiconv
    pkgs.cargo
    pkgs.pkg-config
    pkgs.libffi
    pkgs.cacert
    pkgs.dbus
    pkgs.gnupg
    pkgs.glibcLocales
    pkgs.gitFull
    pkgs.libxcrypt
    pkgs.taskflow
    pkgs.rapidfuzz-cpp
  ];
}

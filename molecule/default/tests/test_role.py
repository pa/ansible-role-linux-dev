import testinfra

def test_linux_dev(host):
    assert host.file("/root/dev/resources/build-from-source").is_directory
    assert host.file("/root/dev/resources/build-from-source/vim/src").is_directory
    assert host.package("myrepos").is_installed
    assert host.package("tmux").is_installed
  
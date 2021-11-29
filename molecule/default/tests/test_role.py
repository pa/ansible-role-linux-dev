import testinfra

def test_linux_dev(host):
    # Check dev directories exists
    assert host.file("/root/dev/archive").is_directory
    assert host.file("/root/dev/config").is_directory
    assert host.file("/root/dev/resources").is_directory
    assert host.file("/root/dev/side").is_directory
    assert host.file("/root/dev/working").is_directory
    assert host.file("/root/dev/tmp").is_directory
    
    # Check all required packages installed
    assert host.package("fish").is_installed
    assert host.package("tmux").is_installed
    assert host.package("nvim").is_installed
    assert host.package("fish").is_installed
    assert host.package("myrepos").is_installed

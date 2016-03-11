# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "ubuntu/vivid64"

  config.vm.network "forwarded_port", guest: 8000, host: 8000, auto_correct: true

  config.vm.synced_folder "Plyushkin", "/var/Plyushkin"

  config.vm.provision "shell", path: "Setup.sh"

  config.vm.provision "shell", run: "always", path: "Run.sh"

end

# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  config.vm.synced_folder ".", "/var/webapps/engus/code", owner: "engus", group: "engus"

  config.vm.network :forwarded_port, guest: 80, host: 8080
  config.vm.network :forwarded_port, guest: 8001, host: 8002
  config.vm.network :private_network, ip: "192.168.33.10"

  config.cache.auto_detect = true

  config.vbguest.iso_path = "#{ENV['HOME']}/Downloads/VBoxGuestAdditions.iso"

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "deployment/provision.yml"
    ansible.extra_vars = { nickname: "development", vm: 1 }
  end
end

# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  #config.vm.synced_folder ".", "/var/webapps/engus/code"

  config.vm.network :forwarded_port, guest: 80, host: 8080
  config.vm.network :forwarded_port, guest: 8000, host: 8001
  config.vm.network :private_network, ip: "192.168.33.10"

  config.cache.auto_detect = true

  #config.vm.provision "ansible" do |ansible|
  #  ansible.playbook = "initial.yml"
  #  ansible.extra_vars = { nickname: "development" }
  #end
end

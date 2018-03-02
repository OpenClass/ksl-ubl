# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.hostname = "ksl-ubl"
  config.vm.network :forwarded_port, guest: 22, host: 2224, id: 'ssh'
  config.vm.network :forwarded_port, guest: 15672, host: 15672
  config.ssh.port = 2224
  config.ssh.insert_key = false
  config.vm.network :private_network, ip: "192.168.1.11"
  config.ssh.forward_agent = true
   
  config.vm.provision "shell", inline: "unlink /usr/bin/python; ln /usr/bin/python3 /usr/bin/python"

  config.vm.provision "ansible" do |ansible|
    ansible.host_key_checking = false
    ansible.playbook = "provision_vagrant.yml"
    ansible.limit = 'all'
    ansible.verbose = 'v'
    ansible.raw_ssh_args = ['-o ForwardAgent=yes']
  end

end

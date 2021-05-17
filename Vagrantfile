# -*- mode: ruby -*-
# vi: set ft=ruby sw=2 st=2 et :
Vagrant.configure('2') do |config|

#------------------ Serveur Jenkins  
    
    config.vm.box_check_update = false
        
                config.vm.define 'srvjenkins' do |machine|
				    machine.vm.box = 'debian/buster64'
                    machine.vm.hostname = 'srvjenkins'
                    machine.vm.network :public_network, ip: "192.168.0.50"
                    machine.vm.provider 'virtualbox' do |vb|
						vb.memory = '3000'
					machine.vm.network :forwarded_port, guest: 8080, host: 8080, host_ip: "192.168.0.50"
						
				    end
					
	            config.vm.provision 'shell', path: 'provision_jenkins.sh'
config.vm.provision "shell", inline: <<-SHELL
echo "#nameserver 10.0.2.3
nameserver 8.8.8.8
nameserver 8.8.4.4" > /etc/resolv.conf
SHELL
                end
end
 
#----------------------Serveur Nexus---------
#VAGRANTFILE_API_VERSION = "2"

#Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
	Vagrant.configure('2') do |config|
		config.vm.box_check_update = false
			config.vm.define "srvnexus" do |srvnexus|
				srvnexus.vm.box = "bento/ubuntu-20.10"
				srvnexus.vm.hostname = "srvnexus"
				srvnexus.vm.box_url = "bento/ubuntu-20.10"
				srvnexus.vm.network :public_network, ip: "192.168.0.51"
				srvnexus.vm.provider :virtualbox do |v|
					v.memory = '1000'
				srvnexus.vm.network :forwarded_port, guest: 8081, host: 8081, host_ip: "192.168.0.51"
					# Shared folder
				srvnexus.vm.synced_folder "project/", "/home/project", create: true
				end
				# Provision
					srvnexus.vm.provision 'shell', path: 'install.sh'
				
			end
		
	
		
	
	end

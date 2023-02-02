Vagrant.configure("2") do |config|

    config.ssh.insert_key = false 

    config.vm.define "master" do |master|
                  master.vm.hostname = "master"
                  master.vm.box = "ubuntu/focal64"
                  master.vm.network "private_network", ip: "172.16.0.10"
                  master.vm.network "public_network", bridge: "wlp2s0", ip: "192.168.100.100"
                  master.vm.provider "virtualbox" do |vb|
                  vb.name = "master"
                  vb.cpus = 2
                  vb.memory = "2048"
          end
        end
        config.vm.define "node" do |node|
                  node.vm.hostname = "node"
                  node.vm.box = "ubuntu/focal64"
                  node.vm.network "private_network", ip: "172.16.0.20"
                  node.vm.network "public_network", bridge: "wlp2s0", ip: "192.168.100.110"
                  node.vm.provider "virtualbox" do |vb|
                  vb.name = "node"
                  vb.cpus = 2
                  vb.memory = "2048"
          end
        end
    end
    

Vagrant.configure("2") do |config|

N = 2

(1..N).each do |node_id|

  config.vm.define "node#{node_id}" do |node|
    node.vm.hostname = "node#{node_id}"
    node.vm.box = "ubuntu/focal64"
    node.vm.network "private_network", ip: "192.168.56.1#{node_id}"
     node.vm.provider "virtualbox" do |vb|
   	 vb.name = "node#{node_id}"
   	 vb.cpus = 2
   	 vb.memory = "2048"


    if node_id == N
      node.vm.provision :ansible do |ansible|
        ansible.limit = "all"
        ansible.playbook = "playbook.yml"
   
       end
     end
              end
     end
   end
end

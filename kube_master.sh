MASTER_IP="10.0.0.10"
NODENAME=$(hostname -s)
PID_CIDR="192.168.0.0/16"

sudo kubeadm config images pull 

echo "Preflight Check Passed: Downloaded all required images."

sudo kubeadm init --apiserver-advertise-address=$MASTER_IP  
--apiserver-cert-extra-sans=$MASTER_IP --apiserver-cert-extra-sans=$(hostname -f) \
$MASTER_IP --pod-network-cidr=$POD_CIDR --node-name=$NODENAME \
--ignore-preflight-errors-swap
 
 mkdir -p $HOME/.kube
 sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
-
sudo chown $(id -u):$(id -g) $HOME/.kube/config

config_path = "/vagrant/configs"

if [ -d "$config_path" ]; then
    rm -f $config_path/*
else
    mkdir -p $config_path
fi

cp -i /etc/kubernetes/admin.conf $config_path/kubeconfig
touch $config_path/kubeadm-init-completed
chmod +x /vagrant/configs/join.sh

kubeadm token create --print-join-command > /vagrant/configs/join.sh

curl https://docs.projectcalico.org/manifests/calico.yaml -0

kubectl apply -f calico.yaml

kubectl apply -f calico.yaml

kubectl taint nodes --all node-role.kubernetes.io/master-

sudo -i -u vagrant bash << EOF
mkdir -p $HOME/.kube
sudo cp -i /vagrant/configs/config/home/vagrant/.kube/config $HOME/.kube/config
sudo chown  1000:1000 $HOME/.kube/config
EOF
sudo systemctl restart systemd-resolved 
sudo swapoff-a && 
sudo systemctl daemon-reload && sudo systemctl restart  
chmod +x /vagrant/configs/join.sh
echo "Kubernetes Master Node Setup Completed."
echo "You can now join worker nodes using the join comma
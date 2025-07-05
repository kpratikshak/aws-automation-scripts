funct_home_dir(){
    tar czvf - /home/${user}|
    ssh username@backup "cat"> 
    /export/home/username/${host}_{$user}_backup.tar.gz"
    }

host = `hostname`
user = `whoami`

{
funct_home_dir
}
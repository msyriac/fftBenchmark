#/bin/bash


for GROUP in gen3 gen4 gen5 gen6; do
    nohup wq sub -r "job_name:fftBenchmark; priority:med; notgroup:[]; group:[$GROUP]" -c "source ~/.bashrc;source ~/.bash_profile; cd $(pwd); python ftb.py $1 $2 $3 " >$(pwd)/output$GROUP.log &

    sleep 0.5 ;

done


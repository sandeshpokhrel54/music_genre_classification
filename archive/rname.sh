counter=0;
for i in ./Data/genres_original/*; 
do 
	mkdir $counter/ 
	ffmpeg -i $i ./$counter/${counter}%04d.png; 
	((counter=counter+1)); 
done

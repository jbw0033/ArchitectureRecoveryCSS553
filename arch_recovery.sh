#run the crawler
java -jar Crawler/target/Crawler-1.0-SNAPSHOT-jar-with-dependencies.jar
#run the mallet
./mallet-2.0.8/bin/mallet import-dir --input ./Crawler/output --keep-sequence --remove-stopwords --output arch.mallet
./mallet-2.0.8/bin/mallet train-topics --input arch.mallet --num-topics 1 --optimize-interval 1 --output-state topic-state.gz  --output-topic-keys arch_keys.txt --output-doc-topics arch_composition.txt

rm topic-state.gz
rm arch.mallet
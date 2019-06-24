# Textual-Entailment-Using-BERT

Software requirements:
This repo is created on Python 3.5+ and PyTorch 1.0.0.

Basic Library Istallation

PyTorch pretrained bert can be installed by pip as follows:
pip install pytorch-pretrained-bert (https://github.com/huggingface/pytorch-pretrained-BERT)

This repository is basically clone from the original repository (https://github.com/huggingface/pytorch-pretrained-BERT)
few changes that have been done are discussed as follows.

Other than MNLI you can use it on other datasets. It not just gives the evaluation result it also saves the prediction.
Some changes are done in run_classifier.py .
All things are just same as mentioned in the above repository.

Given N sentences in any format just comvert that into the following format using file_creation.py 
Column 0: dummy label "entailment".
Column 1: sentence 1
Column 2: sentence 2
Column 3: dummy label "entailment".
Column 4: sentence1_no.
Column 5: sentence2_no.

#Then copy that file to /examples/multinli_1.0 with the name "dev_mismatched.tsv" and an another copy to /examples/ with name "dev_matched.tsv" .

Then use "python3 run_classifier.py --task_name mnli --do_eval --do_lower_case --data_dir multinli_1.0/ --bert_model uncased_L-12_H-768_A-12/ --max_seq_length 128 --train_batch_size 32 --learning_rate 2e-5 --num_train_epochs 3.0 --output_dir MODEL_OUTPUT" to get the file in MODEL_OUTPUT-MM as entail.csv.

This file basically has 5 columns:
Column 0: sentence1_id.
Column 1: sentence2_id.
Column 2: contradiction.
Column 3: entailment.
Column 4: neutral.

Column 2-5 indicate the values of (contradiction,entailment,neutral). We just have to take maximum value out of these three and that will be the output.

To design an sentence to sentence entailment matrix you should use /examples/MODEL_OUTPUT-MM/matrix.py file. That the output is shown in the same folder with "matrix.csv"



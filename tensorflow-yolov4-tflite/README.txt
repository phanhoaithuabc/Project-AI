Dataset:
	B? dataset d� du?c g�n nh�n n?m trong thu m?c VOCdevkit
	T?o ra file annotation cho dataset, cmd run: python voc_annotation.py
Train model:
	Ch?nh c�c class d? train custom model trong file: data/classes/custom.names
	T�y ch?nh c�c super-parameter (epoch, batch size,...) trong file: core/config.py
	cmd run: python train.py

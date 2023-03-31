Dataset:
	B? dataset dã du?c gán nhãn n?m trong thu m?c VOCdevkit
	T?o ra file annotation cho dataset, cmd run: python voc_annotation.py
Train model:
	Ch?nh các class d? train custom model trong file: data/classes/custom.names
	Tùy ch?nh các super-parameter (epoch, batch size,...) trong file: core/config.py
	cmd run: python train.py

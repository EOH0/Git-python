# -*- coding: utf-8 -*-

import os
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from PIL import Image

# 하이퍼파라미터 설정
batch_size = 5
learning_rate = 0.0001
num_epochs = 35

# 데이터 전처리 및 데이터 로더 설정
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
])

# 커스텀 데이터셋 클래스 정의
class CustomImageDataset(datasets.ImageFolder):
    def __init__(self, root, transform=None):
        super().__init__(root, transform=transform)

    def __getitem__(self, index):
        path, target = self.samples[index]
        # JPG 파일만 읽기
        if not path.lower().endswith('.jpg'):
            raise ValueError(f"File {path} is not a JPG image.")
        sample = self.loader(path)
        if self.transform is not None:
            sample = self.transform(sample)
        return sample, target

# 데이터셋 로드
train_dataset = CustomImageDataset(root='C:\\Users\\kogjz\\Downloads\\dataset\\dataset\\train', transform=transform)
train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)

validation_dataset = CustomImageDataset(root="C:\\Users\\kogjz\\Downloads\\dataset\\dataset\\validation", transform=transform)
validation_loader = DataLoader(dataset=validation_dataset, batch_size=batch_size, shuffle=False)

# CNN 모델 정의
class CNNModel(nn.Module):
    def __init__(self):
        super(CNNModel, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(128 * 16 * 16, 128)  # 128 * 16 * 16은 최종 출력 크기
        self.fc2 = nn.Linear(128, len(train_dataset.classes))  # 클래스 수에 맞춰 출력층 설정

    def forward(self, x):
        x = self.pool(nn.functional.relu(self.conv1(x)))
        x = self.pool(nn.functional.relu(self.conv2(x)))
        x = self.pool(nn.functional.relu(self.conv3(x)))
        x = x.view(-1, 128 * 16 * 16)  # Flatten
        x = nn.functional.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# 모델, 손실 함수, 옵티마이저 설정
model = CNNModel()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# 모델 학습
for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    for images, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    
    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {running_loss/len(train_loader):.4f}')

# 모델 저장
torch.save(model.state_dict(), 'cnn_model.pth')

# 검증 단계
model.eval()
correct = 0
total = 0
with torch.no_grad():
    for images, labels in validation_loader:
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f'Accuracy of the model on the validation images: {100 * correct / total:.2f}%')

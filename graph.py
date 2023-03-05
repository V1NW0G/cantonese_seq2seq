import matplotlib.pyplot as plt
import chen
plt.plot(chen.train_losses, label='Training Loss')
plt.plot(chen.eval_losses, label='Evaluation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training and Evaluation Loss')
plt.legend()
plt.show()
print(train_losses)
print(eval_losses)

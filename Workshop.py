import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("FlightInformation.xlsx")
df

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("FlightInformation.xlsx")
df.info()
sns.scatterplot(x=['Price'],y=['Duration'])

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("FlightInformation.xlsx")
sns.scatterplot(x=['Price'],y=['Arrival_Time'])

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("FlightInformation.xlsx")
sns.scatterplot(x=['Price'],y=['Dep_Time'])

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("FlightInformation.xlsx")
states=df.loc[:,["Source","Price"]]
states=states.groupby(by=["Source"]).sum().sort_values(by="Price")
plt.figure(figsize=(17,7))
sns.barplot(x=states.index,y="Price",data=states)
plt.xticks(rotation = 90)
plt.xlabel=("Source")
plt.ylabel=("Price")
plt.show()

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("FlightInformation.xlsx")
states=df.loc[:,["Airline","Price"]]
states=states.groupby(by=["Airline"]).sum().sort_values(by="Price")
plt.figure(figsize=(17,7))
sns.barplot(x=states.index,y="Price",data=states)
plt.xticks(rotation = 90)
plt.xlabel=("Airline")
plt.ylabel=("Price")
plt.show()

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("FlightInformation.xlsx")
states=df.loc[:,["Date_of_Journey","Price"]]
states=states.groupby(by=["Date_of_Journey"]).sum().sort_values(by="Price")
plt.figure(figsize=(17,7))
sns.barplot(x=states.index,y="Price",data=states)
plt.xticks(rotation = 90)
plt.xlabel=("Date_of_Journey")
plt.ylabel=("Price")
plt.show()

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("FlightInformation.xlsx")
states=df.loc[:,["Destination","Price"]]
states=states.groupby(by=["Destination"]).sum().sort_values(by="Price")
plt.figure(figsize=(17,7))
sns.barplot(x=states.index,y="Price",data=states)
plt.xticks(rotation = 90)
plt.xlabel=("Destination")
plt.ylabel=("Price")
plt.show()

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("FlightInformation.xlsx")
states=df.loc[:,["Route","Price"]]
states=states.groupby(by=["Route"]).sum().sort_values(by="Price")
plt.figure(figsize=(17,7))
sns.barplot(x=states.index,y="Price",data=states)
plt.xticks(rotation = 90)
plt.xlabel=("Route")
plt.ylabel=("Price")
plt.show()

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("FlightInformation.xlsx")
states=df.loc[:,["Dep_Time","Price"]]
states=states.groupby(by=["Dep_Time"]).sum().sort_values(by="Price")
plt.figure(figsize=(17,7))
sns.barplot(x=states.index,y="Price",data=states)
plt.xticks(rotation = 90)
plt.xlabel=("Dep_Time")
plt.ylabel=("Price")
plt.show()

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("FlightInformation.xlsx")
states=df.loc[:,["Arrival_Time","Price"]]
states=states.groupby(by=["Arrival_Time"]).sum().sort_values(by="Price")
plt.figure(figsize=(17,7))
sns.barplot(x=states.index,y="Price",data=states)
plt.xticks(rotation = 90)
plt.xlabel=("Arrival_Time")
plt.ylabel=("Price")
plt.show()

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("FlightInformation.xlsx")
states=df.loc[:,["Duration","Price"]]
states=states.groupby(by=["Duration"]).sum().sort_values(by="Price")
plt.figure(figsize=(17,7))
sns.barplot(x=states.index,y="Price",data=states)
plt.xticks(rotation = 90)
plt.xlabel=("Duration")
plt.ylabel=("Price")
plt.show()

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("FlightInformation.xlsx")
states=df.loc[:,["Total_Stops","Price"]]
states=states.groupby(by=["Total_Stops"]).sum().sort_values(by="Price")
plt.figure(figsize=(17,7))
sns.barplot(x=states.index,y="Price",data=states)
plt.xticks(rotation = 90)
plt.xlabel=("Total_Stops")
plt.ylabel=("Price")
plt.show()

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("FlightInformation.xlsx")
states=df.loc[:,["Additional_Info","Price"]]
states=states.groupby(by=["Additional_Info"]).sum().sort_values(by="Price")
plt.figure(figsize=(17,7))
sns.barplot(x=states.index,y="Price",data=states)
plt.xticks(rotation = 90)
plt.xlabel=("Additional_Info")
plt.ylabel=("Price")
plt.show()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("FlightInformation.xlsx")
df.corr()

import pandas as pd
import numpy as np
import seaborn as sns
from google.colab import files
uploaded = files.upload()
df = pd.read_excel("FlightInformation.xlsx")
sns.heatmap(df.corr(),annot=True)

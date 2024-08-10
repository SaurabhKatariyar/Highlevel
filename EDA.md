```python
# !pip install matplotlib
```


```python
import pandas as pd
```


```python
# Load data 
data = pd.read_csv('/home/saurabhk/Downloads/books_task.csv')
```


```python
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>Title</th>
      <th>description</th>
      <th>authors</th>
      <th>publisher</th>
      <th>publishedDate</th>
      <th>categories</th>
      <th>Impact</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Its Only Art If Its Well Hung!</td>
      <td>NaN</td>
      <td>['Julie Strain']</td>
      <td>Smithsonian Institution</td>
      <td>1996</td>
      <td>['Comics &amp; Graphic Novels']</td>
      <td>784.303924</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Dr. Seuss: American Icon</td>
      <td>Philip Nel takes a fascinating look into the k...</td>
      <td>['Philip Nel']</td>
      <td>A&amp;C Black</td>
      <td>2005-01-01</td>
      <td>['Biography &amp; Autobiography']</td>
      <td>825.465535</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Wonderful Worship in Smaller Churches</td>
      <td>This resource includes twelve principles in un...</td>
      <td>['David R. Ray']</td>
      <td>OUP USA</td>
      <td>2000</td>
      <td>['Religion']</td>
      <td>841.705321</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Whispers of the Wicked Saints</td>
      <td>Julia Thomas finds her life spinning out of co...</td>
      <td>['Veronica Haddon']</td>
      <td>iUniverse</td>
      <td>2005-02</td>
      <td>['Fiction']</td>
      <td>666.426542</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>The Church of Christ: A Biblical Ecclesiology ...</td>
      <td>In The Church of Christ: A Biblical Ecclesiolo...</td>
      <td>['Everett Ferguson']</td>
      <td>Wm. B. Eerdmans Publishing</td>
      <td>1996</td>
      <td>['Religion']</td>
      <td>806.216143</td>
    </tr>
  </tbody>
</table>
</div>



## Basic Data Exploration


```python
del data['Unnamed: 0']
```


```python
# Type of data 
data_type = []
for col in data.columns:
    data_type.append({'Column': col,'Datatype': data[col].dtype, 'MissingEntries': data[col].isnull().sum()/data.shape[0]*100})
pd.DataFrame(data_type)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Column</th>
      <th>Datatype</th>
      <th>MissingEntries</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Title</td>
      <td>object</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>description</td>
      <td>object</td>
      <td>9.190191</td>
    </tr>
    <tr>
      <th>2</th>
      <td>authors</td>
      <td>object</td>
      <td>1.962890</td>
    </tr>
    <tr>
      <th>3</th>
      <td>publisher</td>
      <td>object</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>publishedDate</td>
      <td>object</td>
      <td>0.250858</td>
    </tr>
    <tr>
      <th>5</th>
      <td>categories</td>
      <td>object</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Impact</td>
      <td>float64</td>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
def num_entries(txt):
    '''
    Fuction to get the number of authors or categories per book.
    '''
    if isinstance(txt, str):
        return int(len(eval(txt)))
    else:
        return None
```


```python
data['num_authors'] = data['authors'].apply(num_entries)
data['num_categories'] = data['categories'].apply(num_entries)
```


```python
pd.DataFrame(data['num_authors'].value_counts().sort_index(ascending=False))
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
    </tr>
    <tr>
      <th>num_authors</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>110.0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>91.0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>79.0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>57.0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>52.0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>48.0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>39.0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>33.0</th>
      <td>3</td>
    </tr>
    <tr>
      <th>31.0</th>
      <td>2</td>
    </tr>
    <tr>
      <th>28.0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>27.0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>26.0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>25.0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>24.0</th>
      <td>2</td>
    </tr>
    <tr>
      <th>22.0</th>
      <td>2</td>
    </tr>
    <tr>
      <th>21.0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>20.0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>19.0</th>
      <td>3</td>
    </tr>
    <tr>
      <th>18.0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>17.0</th>
      <td>3</td>
    </tr>
    <tr>
      <th>16.0</th>
      <td>3</td>
    </tr>
    <tr>
      <th>15.0</th>
      <td>3</td>
    </tr>
    <tr>
      <th>14.0</th>
      <td>3</td>
    </tr>
    <tr>
      <th>13.0</th>
      <td>5</td>
    </tr>
    <tr>
      <th>12.0</th>
      <td>6</td>
    </tr>
    <tr>
      <th>11.0</th>
      <td>11</td>
    </tr>
    <tr>
      <th>10.0</th>
      <td>13</td>
    </tr>
    <tr>
      <th>9.0</th>
      <td>27</td>
    </tr>
    <tr>
      <th>8.0</th>
      <td>39</td>
    </tr>
    <tr>
      <th>7.0</th>
      <td>73</td>
    </tr>
    <tr>
      <th>6.0</th>
      <td>153</td>
    </tr>
    <tr>
      <th>5.0</th>
      <td>402</td>
    </tr>
    <tr>
      <th>4.0</th>
      <td>1307</td>
    </tr>
    <tr>
      <th>3.0</th>
      <td>5081</td>
    </tr>
    <tr>
      <th>2.0</th>
      <td>21169</td>
    </tr>
    <tr>
      <th>1.0</th>
      <td>107677</td>
    </tr>
  </tbody>
</table>
</div>



#### We see that there can be upto 110 authors for a book. Although there are very few books with authors more than 5. We will explore later on how to hande this


```python
data['num_categories'].value_counts()
```




    num_categories
    1    138724
    Name: count, dtype: int64



#### Unlike authors we have only one category per book, that's great!!

### Extracting list out of string values for authors and categories fields.


```python
def text2List(txt):
    if isinstance(txt, str):
        return eval(txt)
    else:
        return None
```


```python
data['authors'] = data['authors'].apply(text2List)
```


```python
data['categories'] = data['categories'].apply(text2List)
```


```python
# Since there is one catgory per book
# Extracting the category out of list
data['categories'] = data['categories'].apply(lambda x: x[0])
```

#### Again, Checking for the data type now


```python
# Type of data 
data_type = []
for col in data.columns:
    data_type.append({'Column': col,'Datatype': data[col].dtype, 'MissingEntries': data[col].isnull().sum()/data.shape[0]*100})
pd.DataFrame(data_type)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Column</th>
      <th>Datatype</th>
      <th>MissingEntries</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Title</td>
      <td>object</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>description</td>
      <td>object</td>
      <td>9.190191</td>
    </tr>
    <tr>
      <th>2</th>
      <td>authors</td>
      <td>object</td>
      <td>1.962890</td>
    </tr>
    <tr>
      <th>3</th>
      <td>publisher</td>
      <td>object</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>publishedDate</td>
      <td>object</td>
      <td>0.250858</td>
    </tr>
    <tr>
      <th>5</th>
      <td>categories</td>
      <td>object</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Impact</td>
      <td>float64</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>7</th>
      <td>num_authors</td>
      <td>float64</td>
      <td>1.962890</td>
    </tr>
    <tr>
      <th>8</th>
      <td>num_categories</td>
      <td>int64</td>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
      <th>description</th>
      <th>authors</th>
      <th>publisher</th>
      <th>publishedDate</th>
      <th>categories</th>
      <th>Impact</th>
      <th>num_authors</th>
      <th>num_categories</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Its Only Art If Its Well Hung!</td>
      <td>NaN</td>
      <td>[Julie Strain]</td>
      <td>Smithsonian Institution</td>
      <td>1996</td>
      <td>Comics &amp; Graphic Novels</td>
      <td>784.303924</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Dr. Seuss: American Icon</td>
      <td>Philip Nel takes a fascinating look into the k...</td>
      <td>[Philip Nel]</td>
      <td>A&amp;C Black</td>
      <td>2005-01-01</td>
      <td>Biography &amp; Autobiography</td>
      <td>825.465535</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Wonderful Worship in Smaller Churches</td>
      <td>This resource includes twelve principles in un...</td>
      <td>[David R. Ray]</td>
      <td>OUP USA</td>
      <td>2000</td>
      <td>Religion</td>
      <td>841.705321</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Whispers of the Wicked Saints</td>
      <td>Julia Thomas finds her life spinning out of co...</td>
      <td>[Veronica Haddon]</td>
      <td>iUniverse</td>
      <td>2005-02</td>
      <td>Fiction</td>
      <td>666.426542</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>The Church of Christ: A Biblical Ecclesiology ...</td>
      <td>In The Church of Christ: A Biblical Ecclesiolo...</td>
      <td>[Everett Ferguson]</td>
      <td>Wm. B. Eerdmans Publishing</td>
      <td>1996</td>
      <td>Religion</td>
      <td>806.216143</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### Problems with published date
1. No fixed format
2. Not a datetime object
3. Unwanted chars, eg. 1963*, 19??, -01-01 etc


```python
data['publishedDate'].value_counts()
```




    publishedDate
    2000          3362
    2004          3218
    1999          3159
    2002          3110
    2003          3070
                  ... 
    1981-12-18       1
    1969-11-15       1
    2000-03-05       1
    2004-07-24       1
    2007-08-26       1
    Name: count, Length: 10819, dtype: int64




```python
import re

def extract_year(date_str):
    if isinstance(date_str, str):
        match = re.match(r'^(\d{4})[-/*?]', date_str)
        if match:
            return match.group(1)
        return None
    return None

# Example usage
date_str = "19??"
year = extract_year(date_str)
print(f"Year extracted: {year}")

```

    Year extracted: None



```python

```


```python
data['publishedDateFormatted'] = data['publishedDate'].apply(extract_year)
data['IsYear'] = data['publishedDateFormatted'].apply(lambda x: len(x) if isinstance(x, str) else x)
```


```python
data['publishedDateFormatted'].describe()
```




    count     83898
    unique      100
    top        2012
    freq       4623
    Name: publishedDateFormatted, dtype: object




```python
data[data['publishedDateFormatted']>'1970'].sort_values(by='publishedDateFormatted')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
      <th>description</th>
      <th>authors</th>
      <th>publisher</th>
      <th>publishedDate</th>
      <th>categories</th>
      <th>Impact</th>
      <th>num_authors</th>
      <th>num_categories</th>
      <th>publishedDateFormatted</th>
      <th>IsYear</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>22289</th>
      <td>Wisdom of the Mystic Masters</td>
      <td>This book contains the most awesome secrets ev...</td>
      <td>[Joseph J. Weed]</td>
      <td>Penguin</td>
      <td>1971-02-01</td>
      <td>Self-Help</td>
      <td>929.438479</td>
      <td>1.0</td>
      <td>1</td>
      <td>1971</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>134323</th>
      <td>Tibet</td>
      <td>The author describes her experiences during a ...</td>
      <td>[Alexandra David-Neel]</td>
      <td>Courier Corporation</td>
      <td>1971-01-01</td>
      <td>Body, Mind &amp; Spirit</td>
      <td>799.162610</td>
      <td>1.0</td>
      <td>1</td>
      <td>1971</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>69681</th>
      <td>The categorical imperative: A study in Kant's ...</td>
      <td>A classic exposition of Kant's ethical thought.</td>
      <td>[H. J. Paton]</td>
      <td>University of Pennsylvania Press</td>
      <td>1971-10-29</td>
      <td>Philosophy</td>
      <td>799.162610</td>
      <td>1.0</td>
      <td>1</td>
      <td>1971</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>12098</th>
      <td>The Categorical Imperative</td>
      <td>A classic exposition of Kant's ethical thought.</td>
      <td>[H. J. Paton]</td>
      <td>University of Pennsylvania Press</td>
      <td>1971-10-29</td>
      <td>Philosophy</td>
      <td>799.162610</td>
      <td>1.0</td>
      <td>1</td>
      <td>1971</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>88941</th>
      <td>The collected poems of A E Housman</td>
      <td>Presents the texts, authorized in 1939, of the...</td>
      <td>[A. E. Housman]</td>
      <td>Macmillan</td>
      <td>1971-04-15</td>
      <td>Poetry</td>
      <td>805.568540</td>
      <td>1.0</td>
      <td>1</td>
      <td>1971</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>98130</th>
      <td>Peace at Last</td>
      <td>Jill Murphy's bestselling classic Peace at Las...</td>
      <td>[Jill Murphy]</td>
      <td>Pan Macmillan</td>
      <td>2023-08-17</td>
      <td>Juvenile Fiction</td>
      <td>811.867600</td>
      <td>1.0</td>
      <td>1</td>
      <td>2023</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>134235</th>
      <td>I'm Coming to Take You to Lunch</td>
      <td>London, 1983. Pop impresario Simon Napier-Bell...</td>
      <td>[Simon Napier-Bell]</td>
      <td>Wm. B. Eerdmans Publishing</td>
      <td>2023-04-04</td>
      <td>Biography &amp; Autobiography</td>
      <td>819.108336</td>
      <td>1.0</td>
      <td>1</td>
      <td>2023</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>58691</th>
      <td>How the Universe Got Its Spots: Diary of a Fin...</td>
      <td>Mixing memoir and visionary science, a leading...</td>
      <td>[Janna Levin]</td>
      <td>Princeton University Press</td>
      <td>2023-01-10</td>
      <td>Science</td>
      <td>812.846224</td>
      <td>1.0</td>
      <td>1</td>
      <td>2023</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>104651</th>
      <td>University Ghost Story</td>
      <td>Dr. Veronica Glass, professor of English liter...</td>
      <td>[Nick DiMartino]</td>
      <td>Northwest Corner Books</td>
      <td>2023-05-09</td>
      <td>Fiction</td>
      <td>806.216143</td>
      <td>1.0</td>
      <td>1</td>
      <td>2023</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>63709</th>
      <td>A Wealth of Wisdom: Legendary African American...</td>
      <td>The wisdom of our elders is our most valuable ...</td>
      <td>[Camille Cosby, Rene Poussaint]</td>
      <td>Simon and Schuster</td>
      <td>2030-12-31</td>
      <td>Biography &amp; Autobiography</td>
      <td>834.414650</td>
      <td>2.0</td>
      <td>1</td>
      <td>2030</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
<p>83524 rows × 11 columns</p>
</div>




```python
data[data['publishedDateFormatted']>='1950'].groupby('publishedDateFormatted').describe()['Impact']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>publishedDateFormatted</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1950</th>
      <td>7.0</td>
      <td>786.858765</td>
      <td>45.111859</td>
      <td>705.933400</td>
      <td>773.794212</td>
      <td>805.568540</td>
      <td>808.927162</td>
      <td>831.066667</td>
    </tr>
    <tr>
      <th>1951</th>
      <td>11.0</td>
      <td>806.411183</td>
      <td>40.699348</td>
      <td>708.164202</td>
      <td>805.568540</td>
      <td>806.216143</td>
      <td>819.108336</td>
      <td>882.726455</td>
    </tr>
    <tr>
      <th>1952</th>
      <td>6.0</td>
      <td>792.013425</td>
      <td>31.467086</td>
      <td>731.962667</td>
      <td>789.620078</td>
      <td>805.568540</td>
      <td>805.568540</td>
      <td>819.108336</td>
    </tr>
    <tr>
      <th>1953</th>
      <td>7.0</td>
      <td>807.871717</td>
      <td>23.379479</td>
      <td>784.303924</td>
      <td>786.674616</td>
      <td>805.568540</td>
      <td>825.087501</td>
      <td>841.705321</td>
    </tr>
    <tr>
      <th>1954</th>
      <td>9.0</td>
      <td>809.559657</td>
      <td>43.363709</td>
      <td>726.082143</td>
      <td>795.886613</td>
      <td>802.858931</td>
      <td>821.904217</td>
      <td>892.462096</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2020</th>
      <td>2181.0</td>
      <td>787.811061</td>
      <td>59.879261</td>
      <td>276.370338</td>
      <td>763.039309</td>
      <td>805.568540</td>
      <td>819.108336</td>
      <td>951.599804</td>
    </tr>
    <tr>
      <th>2021</th>
      <td>2159.0</td>
      <td>786.197695</td>
      <td>62.913328</td>
      <td>290.116156</td>
      <td>763.039309</td>
      <td>801.960983</td>
      <td>819.108336</td>
      <td>954.489817</td>
    </tr>
    <tr>
      <th>2022</th>
      <td>936.0</td>
      <td>789.454252</td>
      <td>58.679050</td>
      <td>294.001756</td>
      <td>767.147946</td>
      <td>805.568540</td>
      <td>817.899332</td>
      <td>957.892175</td>
    </tr>
    <tr>
      <th>2023</th>
      <td>8.0</td>
      <td>805.906908</td>
      <td>18.626400</td>
      <td>779.216884</td>
      <td>798.980626</td>
      <td>809.041871</td>
      <td>814.411752</td>
      <td>833.214652</td>
    </tr>
    <tr>
      <th>2030</th>
      <td>1.0</td>
      <td>834.414650</td>
      <td>NaN</td>
      <td>834.414650</td>
      <td>834.414650</td>
      <td>834.414650</td>
      <td>834.414650</td>
      <td>834.414650</td>
    </tr>
  </tbody>
</table>
<p>75 rows × 8 columns</p>
</div>




```python
data['publishedDateFormatted'].isnull().sum()/data.shape[0]*100
```




    np.float64(39.521640091116176)




```python
import re
from datetime import datetime

def clean_and_extract_date(date_str):
    # Remove unwanted characters
    cleaned_date_str = re.sub(r'[^\d/-]', '', date_str)
    # Normalize separators to dashes
    cleaned_date_str = re.sub(r'[/]+', '-', cleaned_date_str)
    
    # Patterns to match various date formats
    patterns = [
        r'^(\d{4})-(\d{2})-(\d{2})$',  # YYYY-MM-DD
        r'^(\d{2})-(\d{2})-(\d{4})$',  # DD-MM-YYYY
        r'^(\d{4})-(\d{1,2})-(\d{1,2})$',  # YYYY-MM-DD or YYYY-MM-D
        r'^(\d{1,2})-(\d{1,2})-(\d{4})$',  # DD-MM-YYYY
        r'^(\d{4})$',  # YYYY
        r'^(\d{4})-(\d{1,2})$',  # YYYY-MM
    ]
    
    # Try each pattern
    for pattern in patterns:
        match = re.match(pattern, cleaned_date_str)
        if match:
            groups = match.groups()
            
            # Handle groups based on length
            if len(groups) == 1:
                # Year-only case
                year = groups[0]
                month = '01'
                day = '01'
            elif len(groups) == 2:
                # Year and month only
                year, month = groups
                day = '01'
            elif len(groups) == 3:
                year, month, day = groups
            
            # Handle ambiguous or incomplete dates
            if len(year) == 2:
                year = '20' + year  # Assuming 20th or 21st century
            
            if len(month) == 1:
                month = '0' + month
            
            if len(day) == 1:
                day = '0' + day
            
            try:
                # Create a datetime object to validate the date
                date_obj = datetime(year=int(year), month=int(month), day=int(day))
                return date_obj.year, date_obj.month, date_obj.day
            except ValueError:
                # Date is invalid, continue to next pattern
                continue

    # If no valid date format was found
    return None, None, None

# Example usage
date_strs = [
    "1963*01-01",
    "1996",
    "2001-08",
    "01-12-2003",
    "15/05/1998",
    "2024/02/30",  # Invalid date
    "2024/12",     # Year and month only
    "2000?01*01",  # Contains unwanted characters
    "??2023/03/15" # Contains unwanted characters
]

for date_str in date_strs:
    year, month, day = clean_and_extract_date(date_str)
    print(f"Input: {date_str} -> Year: {year}, Month: {month}, Day: {day}")





```

    Input: 1963*01-01 -> Year: None, Month: None, Day: None
    Input: 1996 -> Year: 1996, Month: 1, Day: 1
    Input: 2001-08 -> Year: 2001, Month: 8, Day: 1
    Input: 01-12-2003 -> Year: None, Month: None, Day: None
    Input: 15/05/1998 -> Year: None, Month: None, Day: None
    Input: 2024/02/30 -> Year: None, Month: None, Day: None
    Input: 2024/12 -> Year: 2024, Month: 12, Day: 1
    Input: 2000?01*01 -> Year: None, Month: None, Day: None
    Input: ??2023/03/15 -> Year: 2023, Month: 3, Day: 15



```python
# for d in dt:
#     print (d, clean_and_extract_date(d))

```


```python
dt = data['publishedDate']
dt = [x.replace('*', '') for x in dt if isinstance(x, str)]
```


```python
# pd.to_datetime(dt, format='mixed')
```


```python
data[data['publishedDate']=='19??']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
      <th>description</th>
      <th>authors</th>
      <th>publisher</th>
      <th>publishedDate</th>
      <th>categories</th>
      <th>Impact</th>
      <th>num_authors</th>
      <th>num_categories</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>11535</th>
      <td>The American method of dog training</td>
      <td>NaN</td>
      <td>[Jay Rapp]</td>
      <td>Wm. B. Eerdmans Publishing</td>
      <td>19??</td>
      <td>Dogs</td>
      <td>819.108336</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>14913</th>
      <td>Within a budding grove,</td>
      <td>“A l’ombre des jeunes fi lles en fl eurs” est ...</td>
      <td>[Proust M.]</td>
      <td>Рипол Классик</td>
      <td>19??</td>
      <td>Fiction</td>
      <td>900.819051</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>24661</th>
      <td>Abide in Love</td>
      <td>NaN</td>
      <td>[Andrew Murray]</td>
      <td>CCEL</td>
      <td>19??</td>
      <td>Bible</td>
      <td>819.108336</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>55382</th>
      <td>Law Firms: The Vault.com Guide to America's To...</td>
      <td>NaN</td>
      <td>None</td>
      <td>Wm. B. Eerdmans Publishing</td>
      <td>19??</td>
      <td>Law</td>
      <td>806.216143</td>
      <td>NaN</td>
      <td>1</td>
    </tr>
    <tr>
      <th>94905</th>
      <td>Fageol &amp; Twin Coach Buses 1922-1956 Photo Archive</td>
      <td>NaN</td>
      <td>[Fageol Motors Company]</td>
      <td>Tan Books &amp; Pub</td>
      <td>19??</td>
      <td>Automobiles</td>
      <td>805.568540</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>110145</th>
      <td>Within a Budding Grove</td>
      <td>“A l’ombre des jeunes fi lles en fl eurs” est ...</td>
      <td>[Proust M.]</td>
      <td>Рипол Классик</td>
      <td>19??</td>
      <td>Fiction</td>
      <td>900.819051</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>118285</th>
      <td>S.U. Workshop Manual (Carburetters and Electri...</td>
      <td>NaN</td>
      <td>[S.U. Carburetter Co. Ltd, S.U. Carburetter Co...</td>
      <td>Tan Books &amp; Pub</td>
      <td>19??</td>
      <td>Automobiles</td>
      <td>805.568540</td>
      <td>2.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>133702</th>
      <td>Melodious Etudes for Trombone Book 1</td>
      <td>120 Melodious Etudes for Trombone, Book 1. Fro...</td>
      <td>[Joannes Rochut]</td>
      <td>Ravenio Books</td>
      <td>19??</td>
      <td>Music</td>
      <td>924.200686</td>
      <td>1.0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python

```


```python
data.groupby(by=['publisher']).describe()['Impact'].sort_values(by='count', ascending=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>publisher</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Tan Books &amp; Pub</th>
      <td>3635.0</td>
      <td>805.429809</td>
      <td>4.409847</td>
      <td>642.030790</td>
      <td>805.568540</td>
      <td>805.568540</td>
      <td>805.568540</td>
      <td>910.511006</td>
    </tr>
    <tr>
      <th>Simon and Schuster</th>
      <td>3600.0</td>
      <td>784.122762</td>
      <td>84.251191</td>
      <td>269.276530</td>
      <td>752.982375</td>
      <td>802.818192</td>
      <td>831.066667</td>
      <td>974.640408</td>
    </tr>
    <tr>
      <th>Smithsonian Institution</th>
      <td>3216.0</td>
      <td>788.289553</td>
      <td>8.187408</td>
      <td>660.386220</td>
      <td>784.303924</td>
      <td>784.303924</td>
      <td>793.504900</td>
      <td>888.426333</td>
    </tr>
    <tr>
      <th>Penguin</th>
      <td>2788.0</td>
      <td>775.029717</td>
      <td>90.700993</td>
      <td>113.200216</td>
      <td>748.133124</td>
      <td>797.650318</td>
      <td>823.629827</td>
      <td>956.315876</td>
    </tr>
    <tr>
      <th>Wm. B. Eerdmans Publishing</th>
      <td>2563.0</td>
      <td>814.085374</td>
      <td>14.387331</td>
      <td>602.943800</td>
      <td>812.285783</td>
      <td>819.108336</td>
      <td>819.108336</td>
      <td>938.891537</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Integritous Press</th>
      <td>1.0</td>
      <td>874.642256</td>
      <td>NaN</td>
      <td>874.642256</td>
      <td>874.642256</td>
      <td>874.642256</td>
      <td>874.642256</td>
      <td>874.642256</td>
    </tr>
    <tr>
      <th>Intellichoice Incorporated</th>
      <td>1.0</td>
      <td>819.108336</td>
      <td>NaN</td>
      <td>819.108336</td>
      <td>819.108336</td>
      <td>819.108336</td>
      <td>819.108336</td>
      <td>819.108336</td>
    </tr>
    <tr>
      <th>Intelligence</th>
      <td>1.0</td>
      <td>805.568540</td>
      <td>NaN</td>
      <td>805.568540</td>
      <td>805.568540</td>
      <td>805.568540</td>
      <td>805.568540</td>
      <td>805.568540</td>
    </tr>
    <tr>
      <th>Intelligence Here</th>
      <td>1.0</td>
      <td>733.514594</td>
      <td>NaN</td>
      <td>733.514594</td>
      <td>733.514594</td>
      <td>733.514594</td>
      <td>733.514594</td>
      <td>733.514594</td>
    </tr>
    <tr>
      <th>Institute of Electrical &amp; Electronics Engineers(IEEE)</th>
      <td>1.0</td>
      <td>805.568540</td>
      <td>NaN</td>
      <td>805.568540</td>
      <td>805.568540</td>
      <td>805.568540</td>
      <td>805.568540</td>
      <td>805.568540</td>
    </tr>
  </tbody>
</table>
<p>12855 rows × 8 columns</p>
</div>




```python
data.groupby(by=['categories']).describe()['Impact'].sort_values(by='count', ascending=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>categories</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Fiction</th>
      <td>23419.0</td>
      <td>774.283955</td>
      <td>77.453271</td>
      <td>0.000000</td>
      <td>749.415203</td>
      <td>791.455372</td>
      <td>819.108336</td>
      <td>997.901870</td>
    </tr>
    <tr>
      <th>Religion</th>
      <td>9459.0</td>
      <td>799.077709</td>
      <td>56.104312</td>
      <td>103.719420</td>
      <td>784.303924</td>
      <td>805.568540</td>
      <td>823.960732</td>
      <td>1000.000000</td>
    </tr>
    <tr>
      <th>History</th>
      <td>9330.0</td>
      <td>787.171576</td>
      <td>55.624224</td>
      <td>5.333957</td>
      <td>767.147946</td>
      <td>800.434471</td>
      <td>817.597974</td>
      <td>991.176647</td>
    </tr>
    <tr>
      <th>Juvenile Fiction</th>
      <td>6643.0</td>
      <td>806.536147</td>
      <td>60.812831</td>
      <td>230.382115</td>
      <td>784.303924</td>
      <td>806.216143</td>
      <td>837.128640</td>
      <td>983.672175</td>
    </tr>
    <tr>
      <th>Biography &amp; Autobiography</th>
      <td>6324.0</td>
      <td>788.595072</td>
      <td>69.956489</td>
      <td>195.465314</td>
      <td>763.085492</td>
      <td>805.568540</td>
      <td>823.960732</td>
      <td>972.809618</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Christianity</th>
      <td>79.0</td>
      <td>791.241690</td>
      <td>58.550684</td>
      <td>474.551626</td>
      <td>763.039309</td>
      <td>805.568540</td>
      <td>819.108336</td>
      <td>899.135022</td>
    </tr>
    <tr>
      <th>Young Adult Nonfiction</th>
      <td>79.0</td>
      <td>812.227203</td>
      <td>42.693500</td>
      <td>700.791613</td>
      <td>784.303924</td>
      <td>805.568540</td>
      <td>832.740659</td>
      <td>948.691125</td>
    </tr>
    <tr>
      <th>Railroads</th>
      <td>78.0</td>
      <td>798.849232</td>
      <td>23.848189</td>
      <td>683.064566</td>
      <td>784.303924</td>
      <td>805.568540</td>
      <td>805.568540</td>
      <td>859.810559</td>
    </tr>
    <tr>
      <th>Brothers and sisters</th>
      <td>76.0</td>
      <td>801.559159</td>
      <td>56.398428</td>
      <td>517.856252</td>
      <td>784.303924</td>
      <td>805.568540</td>
      <td>826.037090</td>
      <td>917.614808</td>
    </tr>
    <tr>
      <th>Automobiles</th>
      <td>74.0</td>
      <td>793.049254</td>
      <td>34.961506</td>
      <td>699.748608</td>
      <td>780.488644</td>
      <td>805.568540</td>
      <td>811.867600</td>
      <td>860.106001</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 8 columns</p>
</div>




```python
data.groupby(by=['publisher','categories']).describe()['Impact'].sort_values(by='count', ascending=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>publisher</th>
      <th>categories</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Penguin</th>
      <th>Fiction</th>
      <td>1114.0</td>
      <td>756.051956</td>
      <td>104.192616</td>
      <td>113.200216</td>
      <td>722.790025</td>
      <td>783.315457</td>
      <td>817.746626</td>
      <td>939.106578</td>
    </tr>
    <tr>
      <th>Simon and Schuster</th>
      <th>Fiction</th>
      <td>915.0</td>
      <td>758.797783</td>
      <td>90.519469</td>
      <td>280.780097</td>
      <td>720.510077</td>
      <td>779.216884</td>
      <td>811.867600</td>
      <td>954.044450</td>
    </tr>
    <tr>
      <th>Open Road Media</th>
      <th>Fiction</th>
      <td>624.0</td>
      <td>777.235909</td>
      <td>65.202815</td>
      <td>400.658954</td>
      <td>750.331270</td>
      <td>788.758430</td>
      <td>816.497238</td>
      <td>929.586770</td>
    </tr>
    <tr>
      <th>Harper Collins</th>
      <th>Fiction</th>
      <td>618.0</td>
      <td>749.677824</td>
      <td>101.067623</td>
      <td>159.736717</td>
      <td>709.620008</td>
      <td>772.884077</td>
      <td>806.941042</td>
      <td>948.362580</td>
    </tr>
    <tr>
      <th>John Wiley &amp; Sons</th>
      <th>Business &amp; Economics</th>
      <td>573.0</td>
      <td>782.873410</td>
      <td>68.562577</td>
      <td>466.563934</td>
      <td>755.943132</td>
      <td>799.162610</td>
      <td>821.904217</td>
      <td>939.486514</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>tredition</th>
      <th>Technology &amp; Engineering</th>
      <td>1.0</td>
      <td>793.504900</td>
      <td>NaN</td>
      <td>793.504900</td>
      <td>793.504900</td>
      <td>793.504900</td>
      <td>793.504900</td>
      <td>793.504900</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">www.Militarybookshop.CompanyUK</th>
      <th>Business &amp; Economics</th>
      <td>1.0</td>
      <td>805.568540</td>
      <td>NaN</td>
      <td>805.568540</td>
      <td>805.568540</td>
      <td>805.568540</td>
      <td>805.568540</td>
      <td>805.568540</td>
    </tr>
    <tr>
      <th>Transportation</th>
      <td>1.0</td>
      <td>805.568540</td>
      <td>NaN</td>
      <td>805.568540</td>
      <td>805.568540</td>
      <td>805.568540</td>
      <td>805.568540</td>
      <td>805.568540</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">www.bnpublishing.com</th>
      <th>Foreign Language Study</th>
      <td>1.0</td>
      <td>779.216884</td>
      <td>NaN</td>
      <td>779.216884</td>
      <td>779.216884</td>
      <td>779.216884</td>
      <td>779.216884</td>
      <td>779.216884</td>
    </tr>
    <tr>
      <th>Self-Help</th>
      <td>1.0</td>
      <td>752.471772</td>
      <td>NaN</td>
      <td>752.471772</td>
      <td>752.471772</td>
      <td>752.471772</td>
      <td>752.471772</td>
      <td>752.471772</td>
    </tr>
  </tbody>
</table>
<p>32401 rows × 8 columns</p>
</div>




```python
data.groupby(by=['categories','publisher']).describe()['Impact'].sort_values(by='count', ascending=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>categories</th>
      <th>publisher</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">Fiction</th>
      <th>Penguin</th>
      <td>1114.0</td>
      <td>756.051956</td>
      <td>104.192616</td>
      <td>113.200216</td>
      <td>722.790025</td>
      <td>783.315457</td>
      <td>817.746626</td>
      <td>939.106578</td>
    </tr>
    <tr>
      <th>Simon and Schuster</th>
      <td>915.0</td>
      <td>758.797783</td>
      <td>90.519469</td>
      <td>280.780097</td>
      <td>720.510077</td>
      <td>779.216884</td>
      <td>811.867600</td>
      <td>954.044450</td>
    </tr>
    <tr>
      <th>Open Road Media</th>
      <td>624.0</td>
      <td>777.235909</td>
      <td>65.202815</td>
      <td>400.658954</td>
      <td>750.331270</td>
      <td>788.758430</td>
      <td>816.497238</td>
      <td>929.586770</td>
    </tr>
    <tr>
      <th>Harper Collins</th>
      <td>618.0</td>
      <td>749.677824</td>
      <td>101.067623</td>
      <td>159.736717</td>
      <td>709.620008</td>
      <td>772.884077</td>
      <td>806.941042</td>
      <td>948.362580</td>
    </tr>
    <tr>
      <th>Business &amp; Economics</th>
      <th>John Wiley &amp; Sons</th>
      <td>573.0</td>
      <td>782.873410</td>
      <td>68.562577</td>
      <td>466.563934</td>
      <td>755.943132</td>
      <td>799.162610</td>
      <td>821.904217</td>
      <td>939.486514</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">Adventure stories</th>
      <th>HarperCollins UK</th>
      <td>1.0</td>
      <td>847.476693</td>
      <td>NaN</td>
      <td>847.476693</td>
      <td>847.476693</td>
      <td>847.476693</td>
      <td>847.476693</td>
      <td>847.476693</td>
    </tr>
    <tr>
      <th>Derrydale Press</th>
      <td>1.0</td>
      <td>867.188361</td>
      <td>NaN</td>
      <td>867.188361</td>
      <td>867.188361</td>
      <td>867.188361</td>
      <td>867.188361</td>
      <td>867.188361</td>
    </tr>
    <tr>
      <th>David R. Godine Publisher</th>
      <td>1.0</td>
      <td>923.514537</td>
      <td>NaN</td>
      <td>923.514537</td>
      <td>923.514537</td>
      <td>923.514537</td>
      <td>923.514537</td>
      <td>923.514537</td>
    </tr>
    <tr>
      <th>Collins</th>
      <td>1.0</td>
      <td>714.204668</td>
      <td>NaN</td>
      <td>714.204668</td>
      <td>714.204668</td>
      <td>714.204668</td>
      <td>714.204668</td>
      <td>714.204668</td>
    </tr>
    <tr>
      <th>Berkley</th>
      <td>1.0</td>
      <td>784.303924</td>
      <td>NaN</td>
      <td>784.303924</td>
      <td>784.303924</td>
      <td>784.303924</td>
      <td>784.303924</td>
      <td>784.303924</td>
    </tr>
  </tbody>
</table>
<p>32401 rows × 8 columns</p>
</div>




```python
for col in data.columns:
    print(col,':::', data[col].dtype,':::', data[col].isnull().sum()/data.shape[0]*100)
```

    Title ::: object ::: 0.0
    description ::: object ::: 9.190190594273522
    authors ::: object ::: 1.9628903434157032
    publisher ::: object ::: 0.0
    publishedDate ::: object ::: 0.2508578184020069
    categories ::: object ::: 0.0
    Impact ::: float64 ::: 0.0
    num_authors ::: float64 ::: 1.9628903434157032
    num_categories ::: int64 ::: 0.0



```python
data['Title'].nunique() == data.shape[0]
```




    True




```python
data[data['authors'].isnull()]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
      <th>description</th>
      <th>authors</th>
      <th>publisher</th>
      <th>publishedDate</th>
      <th>categories</th>
      <th>Impact</th>
      <th>num_authors</th>
      <th>num_categories</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>69</th>
      <td>Behind the Moon</td>
      <td>In the fishing village where he lives, David s...</td>
      <td>None</td>
      <td>Dorling Kindersley Ltd</td>
      <td>1895</td>
      <td>Adventure stories</td>
      <td>774.724016</td>
      <td>NaN</td>
      <td>1</td>
    </tr>
    <tr>
      <th>104</th>
      <td>Gorilla</td>
      <td>Little Gorilla's family and friends try to hel...</td>
      <td>None</td>
      <td>Houghton Mifflin Harcourt</td>
      <td>1986-03</td>
      <td>Juvenile Fiction</td>
      <td>897.492511</td>
      <td>NaN</td>
      <td>1</td>
    </tr>
    <tr>
      <th>143</th>
      <td>Haiku: One Breath Poetry</td>
      <td>An exploration of the traditional Japanese thr...</td>
      <td>None</td>
      <td>Heian International Publishing Company</td>
      <td>1997</td>
      <td>Language Arts &amp; Disciplines</td>
      <td>805.568540</td>
      <td>NaN</td>
      <td>1</td>
    </tr>
    <tr>
      <th>152</th>
      <td>Lucianos Luck (6 Cassette)</td>
      <td>NaN</td>
      <td>None</td>
      <td>Mohr Siebeck</td>
      <td>1999</td>
      <td>Audiobooks</td>
      <td>685.670947</td>
      <td>NaN</td>
      <td>1</td>
    </tr>
    <tr>
      <th>171</th>
      <td>Jambalaya: Hal Leonard Student Piano Library C...</td>
      <td>Vols. for 1981- include as no. 2 of each vol. ...</td>
      <td>None</td>
      <td>Tan Books &amp; Pub</td>
      <td>2006</td>
      <td>Music</td>
      <td>805.568540</td>
      <td>NaN</td>
      <td>1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>138286</th>
      <td>The Seven Secrets: Uncovering Genuine Greatnes...</td>
      <td>NaN</td>
      <td>None</td>
      <td>Berg Pub Limited</td>
      <td>2007</td>
      <td>Audiobooks</td>
      <td>766.960634</td>
      <td>NaN</td>
      <td>1</td>
    </tr>
    <tr>
      <th>138412</th>
      <td>Major Anders Lindgren's Teaching Exercises: A ...</td>
      <td>NaN</td>
      <td>None</td>
      <td>Bloomsbury Publishing</td>
      <td>1998</td>
      <td>American literature</td>
      <td>735.237786</td>
      <td>NaN</td>
      <td>1</td>
    </tr>
    <tr>
      <th>138517</th>
      <td>Dragon Knights (Dragon Knights (Graphic Novels...</td>
      <td>"First published in Japan in 1991 by Shinshoka...</td>
      <td>None</td>
      <td>Turtleback Books</td>
      <td>2004-02</td>
      <td>Comics &amp; Graphic Novels</td>
      <td>805.568540</td>
      <td>NaN</td>
      <td>1</td>
    </tr>
    <tr>
      <th>138709</th>
      <td>Anticipation of the Civil War in Mormon though...</td>
      <td>NaN</td>
      <td>None</td>
      <td>Tan Books &amp; Pub</td>
      <td>1983</td>
      <td>Religion</td>
      <td>805.568540</td>
      <td>NaN</td>
      <td>1</td>
    </tr>
    <tr>
      <th>138722</th>
      <td>Red Boots for Christmas</td>
      <td>Everyone in the village of Friedensdorf is hap...</td>
      <td>None</td>
      <td>Wm. B. Eerdmans Publishing</td>
      <td>1995</td>
      <td>Juvenile Fiction</td>
      <td>819.108336</td>
      <td>NaN</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>2723 rows × 9 columns</p>
</div>




```python
data['publisher'].value_counts()
```




    publisher
    Tan Books & Pub               3635
    Simon and Schuster            3600
    Smithsonian Institution       3216
    Penguin                       2788
    Wm. B. Eerdmans Publishing    2563
                                  ... 
    Rider                            1
    Robert Davies Pub                1
    Astrology Sight                  1
    McQueen Enterprises              1
    Torah Aura Prod                  1
    Name: count, Length: 12855, dtype: int64




```python
data.groupby(['publisher'])['authors'].isnull().transform('sum')
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Cell In[20], line 1
    ----> 1 data.groupby(['publisher'])[['authors']].isnull().transform('sum')


    File ~/highlevel/lib/python3.10/site-packages/pandas/core/groupby/groupby.py:1363, in GroupBy.__getattr__(self, attr)
       1360 if attr in self.obj:
       1361     return self[attr]
    -> 1363 raise AttributeError(
       1364     f"'{type(self).__name__}' object has no attribute '{attr}'"
       1365 )


    AttributeError: 'DataFrameGroupBy' object has no attribute 'isnull'



```python
temp = data[data['authors'].isnull()].groupby('publisher').count()
temp.sort_values(by='Title', ascending=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
      <th>description</th>
      <th>authors</th>
      <th>publishedDate</th>
      <th>categories</th>
      <th>Impact</th>
    </tr>
    <tr>
      <th>publisher</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Tan Books &amp; Pub</th>
      <td>390</td>
      <td>51</td>
      <td>0</td>
      <td>390</td>
      <td>390</td>
      <td>390</td>
    </tr>
    <tr>
      <th>Smithsonian Institution</th>
      <td>318</td>
      <td>39</td>
      <td>0</td>
      <td>318</td>
      <td>318</td>
      <td>318</td>
    </tr>
    <tr>
      <th>Wm. B. Eerdmans Publishing</th>
      <td>172</td>
      <td>42</td>
      <td>0</td>
      <td>172</td>
      <td>172</td>
      <td>172</td>
    </tr>
    <tr>
      <th>Berg Pub Limited</th>
      <td>120</td>
      <td>9</td>
      <td>0</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
    </tr>
    <tr>
      <th>OUP USA</th>
      <td>92</td>
      <td>9</td>
      <td>0</td>
      <td>92</td>
      <td>92</td>
      <td>92</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Aeon Books</th>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Addison Wesley Publishing Company</th>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Abrams ComicArts</th>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Abrams Appleseed</th>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Aa Pub</th>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>591 rows × 6 columns</p>
</div>




```python
temp = data[data['description'].isnull()].groupby(['publisher', 'authors']).count()
temp.sort_values(by='Title', ascending=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Title</th>
      <th>description</th>
      <th>publishedDate</th>
      <th>categories</th>
      <th>Impact</th>
    </tr>
    <tr>
      <th>publisher</th>
      <th>authors</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Copyright Office, Library of Congress</th>
      <th>['Library of Congress. Copyright Office']</th>
      <td>87</td>
      <td>0</td>
      <td>87</td>
      <td>87</td>
      <td>87</td>
    </tr>
    <tr>
      <th>Tan Books &amp; Pub</th>
      <th>['Rose Arny']</th>
      <td>51</td>
      <td>0</td>
      <td>51</td>
      <td>51</td>
      <td>51</td>
    </tr>
    <tr>
      <th>Smithsonian Institution</th>
      <th>['Rose Arny']</th>
      <td>45</td>
      <td>0</td>
      <td>45</td>
      <td>45</td>
      <td>45</td>
    </tr>
    <tr>
      <th>Wm. B. Eerdmans Publishing</th>
      <th>['Rose Arny']</th>
      <td>34</td>
      <td>0</td>
      <td>34</td>
      <td>34</td>
      <td>34</td>
    </tr>
    <tr>
      <th>Berg Pub Limited</th>
      <th>['Rose Arny']</th>
      <td>23</td>
      <td>0</td>
      <td>23</td>
      <td>23</td>
      <td>23</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>International Labour Organization</th>
      <th>['Andrew D. F. Price']</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>International Marine Publishing Company</th>
      <th>['John M. Leavens']</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">International Medical Pub</th>
      <th>['James F Masterson', 'Thomas Masterson, M.D.', 'Todd Rothenhaus', 'Todd Rothenhaus, M.D.']</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>['Mario R. Llaneras', 'Ramin Oskoui', 'Thomas Masterson, M.D.', 'Ronald Chamberlain']</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>InterVarsity Press</th>
      <th>['Gordon J. Wenham']</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>10236 rows × 5 columns</p>
</div>




```python
temp = data[data['publishedDate'].isnull()].groupby('publisher').count()
temp.sort_values(by='Title', ascending=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
      <th>description</th>
      <th>authors</th>
      <th>publishedDate</th>
      <th>categories</th>
      <th>Impact</th>
    </tr>
    <tr>
      <th>publisher</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Speaking Volumes</th>
      <td>27</td>
      <td>22</td>
      <td>27</td>
      <td>0</td>
      <td>27</td>
      <td>27</td>
    </tr>
    <tr>
      <th>Alfred Music</th>
      <td>26</td>
      <td>26</td>
      <td>26</td>
      <td>0</td>
      <td>26</td>
      <td>26</td>
    </tr>
    <tr>
      <th>Prometheus Books</th>
      <td>20</td>
      <td>19</td>
      <td>20</td>
      <td>0</td>
      <td>20</td>
      <td>20</td>
    </tr>
    <tr>
      <th>SUNY Press</th>
      <td>15</td>
      <td>15</td>
      <td>14</td>
      <td>0</td>
      <td>15</td>
      <td>15</td>
    </tr>
    <tr>
      <th>Kregel Publications</th>
      <td>12</td>
      <td>12</td>
      <td>11</td>
      <td>0</td>
      <td>12</td>
      <td>12</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Yale University Press</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>eBookIt.com</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>iUniverse</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>全能神教會</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>大賢者外語</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>166 rows × 6 columns</p>
</div>




```python
data[data['description'].isnull()].shape
```




    (12749, 7)




```python
data['authors_str'] = data['authors'].apply(lambda authors: ' '.join(authors) if isinstance(authors, list) else authors)
```


```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectKBest, f_regression

# Convert lists of authors to a single string
data['authors_str'] = data['authors'].apply(lambda authors: ' '.join(authors) if isinstance(authors, list) else authors)
print(data.shape)
df = data.dropna(subset=['authors'])
print(df.shape)
y = df['Impact']
del df['Impact']
# Apply TF-IDF Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['authors_str'])

selector = SelectKBest(f_regression, k=100) 
X_new = selector.fit_transform(X, y)

# Convert to DataFrame
tfidf_df = pd.DataFrame(X_new.toarray(), columns=selector.get_feature_names_out())

# Concatenate with original DataFrame
df = pd.concat([df, tfidf_df], axis=1)

```

    (138724, 12)
    (136001, 12)



```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Title</th>
      <th>description</th>
      <th>authors</th>
      <th>publisher</th>
      <th>publishedDate</th>
      <th>categories</th>
      <th>num_authors</th>
      <th>num_categories</th>
      <th>publishedDateFormatted</th>
      <th>IsYear</th>
      <th>...</th>
      <th>x51525</th>
      <th>x52765</th>
      <th>x53505</th>
      <th>x54177</th>
      <th>x55237</th>
      <th>x55281</th>
      <th>x55591</th>
      <th>x57394</th>
      <th>x58507</th>
      <th>x59400</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Its Only Art If Its Well Hung!</td>
      <td>NaN</td>
      <td>[Julie Strain]</td>
      <td>Smithsonian Institution</td>
      <td>1996</td>
      <td>Comics &amp; Graphic Novels</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>None</td>
      <td>NaN</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Dr. Seuss: American Icon</td>
      <td>Philip Nel takes a fascinating look into the k...</td>
      <td>[Philip Nel]</td>
      <td>A&amp;C Black</td>
      <td>2005-01-01</td>
      <td>Biography &amp; Autobiography</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2005</td>
      <td>4.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Wonderful Worship in Smaller Churches</td>
      <td>This resource includes twelve principles in un...</td>
      <td>[David R. Ray]</td>
      <td>OUP USA</td>
      <td>2000</td>
      <td>Religion</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>None</td>
      <td>NaN</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Whispers of the Wicked Saints</td>
      <td>Julia Thomas finds her life spinning out of co...</td>
      <td>[Veronica Haddon]</td>
      <td>iUniverse</td>
      <td>2005-02</td>
      <td>Fiction</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2005</td>
      <td>4.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>The Church of Christ: A Biblical Ecclesiology ...</td>
      <td>In The Church of Christ: A Biblical Ecclesiolo...</td>
      <td>[Everett Ferguson]</td>
      <td>Wm. B. Eerdmans Publishing</td>
      <td>1996</td>
      <td>Religion</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>None</td>
      <td>NaN</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 111 columns</p>
</div>



# Investigating relationship of categories on Impact


```python
print(data.groupby('categories').describe()['Impact'].sort_values('mean', ascending=False).to_string())
```

                                     count        mean        std         min         25%         50%         75%          max
    categories                                                                                                                
    Young Adult Nonfiction            79.0  812.227203  42.693500  700.791613  784.303924  805.568540  832.740659   948.691125
    Bibles                           406.0  807.536193  50.422445  553.366053  784.303924  805.568540  831.066667   935.318236
    Christian life                   206.0  806.908027  44.463144  553.737562  800.523316  805.568540  819.108336   948.585761
    Juvenile Fiction                6643.0  806.536147  60.812831  230.382115  784.303924  806.216143  837.128640   983.672175
    Animals                          221.0  806.255683  44.806969  659.542530  788.471554  805.568540  823.960732   958.849736
    Cats                             101.0  805.773994  36.360646  699.600482  793.504900  805.568540  819.108336   935.220574
    Children's stories               252.0  803.651468  45.908059  609.170660  784.303924  805.568540  824.088754   929.047398
    Poetry                          1500.0  803.527345  48.962190  281.896278  788.471554  805.568540  823.712554   953.901309
    Families                          84.0  802.823451  54.291116  503.558198  784.303924  805.568540  824.336933   918.551161
    Children's literature            107.0  802.782403  49.710743  589.731329  784.303924  805.568540  819.108336   943.571813
    Cooking                         2445.0  802.717968  57.201454  415.863377  779.216884  805.568540  833.323836   963.203127
    Self-Help                       1519.0  802.607217  61.655518  331.636406  780.695346  805.568540  834.414650   960.586393
    Frontier and pioneer life        107.0  802.388102  31.638433  651.283566  784.303924  805.568540  811.712763   897.492511
    Brothers and sisters              76.0  801.559159  56.398428  517.856252  784.303924  805.568540  826.037090   917.614808
    African Americans                185.0  800.696463  38.422824  674.854410  784.303924  805.568540  819.108336   912.310131
    Children                         126.0  800.347703  35.634741  659.542530  784.303924  805.568540  819.108336   874.642256
    Conduct of life                  114.0  800.164294  47.801371  604.165056  784.303924  805.568540  817.597974   940.163701
    English poetry                    95.0  800.042385  43.599241  642.062184  793.504900  805.568540  819.108336   921.097888
    Dogs                              90.0  799.610531  44.099122  662.053958  784.303924  805.568540  819.108336   914.673273
    Nature                          1146.0  799.202789  52.005789  402.347058  779.216884  805.568540  825.465535   946.805818
    Religion                        9459.0  799.077709  56.104312  103.719420  784.303924  805.568540  823.960732  1000.000000
    Railroads                         78.0  798.849232  23.848189  683.064566  784.303924  805.568540  805.568540   859.810559
    Gardening                        532.0  798.843327  48.417074  465.329838  783.964622  805.568540  822.291683   938.891537
    Juvenile Nonfiction             3446.0  798.632765  53.160190  216.320455  783.964622  805.568540  819.108336   980.726430
    Adventure stories                122.0  798.608143  48.225144  665.137936  777.363117  805.568540  819.108336   945.173876
    Literary Collections             607.0  797.914208  45.565398  517.503816  779.216884  805.568540  819.108336   924.139346
    Canada                            82.0  797.832041  43.359369  547.864610  784.303924  805.568540  810.606472   940.714509
    American poetry                  143.0  797.352089  47.667215  494.820870  784.303924  805.568540  819.108336   903.598507
    Jews                              80.0  796.681531  39.369945  630.759017  784.303924  805.568540  819.108336   888.849805
    Art                             2054.0  795.443523  47.922130  460.419987  779.216884  805.568540  819.108336   956.914379
    Electronic books                 100.0  795.254602  43.399192  593.730809  784.303924  805.568540  806.679794   906.480115
    Bible                            667.0  794.858152  44.412847  480.638320  784.303924  805.568540  819.108336   927.950349
    Body, Mind & Spirit             2049.0  793.911004  65.543680  297.395160  767.147946  805.568540  831.066667   968.644731
    Family & Relationships          2178.0  793.176493  67.274990  279.800260  764.877254  805.568540  831.066667   956.005827
    Automobiles                       74.0  793.049254  34.961506  699.748608  780.488644  805.568540  811.867600   860.106001
    Comic books, strips, etc          98.0  792.961251  63.405973  359.827439  776.977433  800.781298  819.108336   909.779983
    Health & Fitness                2030.0  792.948489  63.280809  284.880893  763.729453  805.568540  831.033492   953.667061
    Indians of North America         118.0  792.790173  37.390415  612.367926  775.847233  805.568540  805.568540   890.295420
    World War, 1939-1945             183.0  792.507577  42.263095  563.089032  779.216884  805.568540  812.285783   891.626641
    Crafts & Hobbies                1350.0  792.242917  60.302960  516.429145  763.039309  805.568540  823.960732   963.463902
    Psychology                      1913.0  791.977803  55.643072  275.570444  774.724016  805.568540  819.108336   945.678850
    Libraries                         91.0  791.859313  45.785712  636.076748  779.216884  805.568540  812.285783   911.086804
    Education                       2611.0  791.387047  51.472851  414.964361  778.285482  805.568540  819.108336   962.873667
    Christianity                      79.0  791.241690  58.550684  474.551626  763.039309  805.568540  819.108336   899.135022
    Literary Criticism              2147.0  791.241268  43.017123  432.156658  779.216884  805.568540  812.285783   957.161005
    California                       102.0  791.018537  59.515015  382.497706  780.348341  805.568540  814.124229   925.559660
    France                           120.0  790.755072  42.599116  646.514840  771.802839  795.886613  805.568540   933.339296
    Copyright                        160.0  790.746859  47.601964  483.689158  784.303924  805.568540  805.568540   907.242825
    Europe                            85.0  790.709754  45.199030  646.514840  763.039309  787.188392  805.568540   940.163701
    Photography                      756.0  790.564585  55.376117  325.267182  774.347090  805.568540  819.108336   952.343887
    Comics & Graphic Novels         1162.0  790.503165  54.643158  307.629607  770.726964  799.162610  819.108336   975.642296
    Authors                           90.0  790.502879  49.549629  521.484815  764.066468  802.119946  816.269927   874.642256
    Philosophy                      1864.0  790.497296  53.121488  316.431553  774.724016  805.568540  819.108336   951.344084
    Medical                         2079.0  790.441911  51.164355  405.074620  770.726964  805.568540  819.108336   948.814190
    Sports & Recreation             2267.0  790.416690  59.904263  354.580423  763.039309  805.568540  822.172316   974.640408
    Design                           322.0  790.283119  50.399778  491.682932  773.533951  805.568540  819.108336   945.496447
    Humor                            799.0  789.848515  69.128936  360.089261  763.039309  805.568540  831.023020   959.955912
    Drama                            685.0  789.782047  48.892565  561.220975  769.835102  805.568540  819.108336   946.478310
    Music                           2106.0  789.356784  56.192970  388.553886  770.726964  805.568540  819.108336   945.321174
    Architecture                     963.0  789.333330  49.004455  405.074620  770.726964  805.568540  819.108336   917.385588
    Biography & Autobiography       6324.0  788.595072  69.956489  195.465314  763.085492  805.568540  823.960732   972.809618
    Great Britain                    268.0  788.429490  41.887502  517.856252  779.216884  799.162610  806.216143   919.510089
    United States                    387.0  787.973481  47.289016  497.011452  773.806245  805.568540  806.216143   926.277530
    Science fiction, American         82.0  787.973095  43.945084  654.403452  762.135110  794.695756  815.444374   911.564239
    Detective and mystery stories    235.0  787.948652  46.982227  594.835459  763.039309  799.162610  812.285783   892.392865
    Language Arts & Disciplines     2036.0  787.748422  49.706333  268.235614  766.243540  800.781298  812.285783   957.000603
    China                             97.0  787.290603  39.938740  646.714279  767.147946  788.471554  805.568540   921.097888
    History                         9330.0  787.171576  55.624224    5.333957  767.147946  800.434471  817.597974   991.176647
    Authors, American                107.0  786.981402  38.739179  656.598438  763.039309  799.162610  813.159832   859.810559
    Performing Arts                 1305.0  786.937774  60.436626  373.264871  761.006527  801.960983  819.108336   938.757929
    American literature              737.0  786.404926  49.183678  501.944563  763.039309  805.568540  806.216143   952.325780
    England                          112.0  785.916059  60.320370  443.274790  767.147946  803.174919  807.280011   906.480115
    Pets                             630.0  785.773541  63.484546  505.664478  755.943132  791.492041  823.960732   945.658585
    Science                         2623.0  784.595943  56.885611  215.169000  763.039309  799.162610  814.734264   934.032344
    English language                 416.0  784.204356  45.573740  579.240917  763.039309  799.162610  805.568540   917.795702
    American fiction                 139.0  783.829453  46.886359  607.061891  764.053776  784.303924  805.568540   911.998261
    Business & Economics            5625.0  783.411560  62.319109  328.549702  759.271158  799.162610  819.108336   983.316577
    Social Science                  3834.0  783.223497  56.822558  358.754659  763.039309  799.162610  812.285783   945.678850
    Young Adult Fiction              595.0  783.161173  79.386296  334.751839  761.239831  805.568540  826.435262   946.835299
    Transportation                   921.0  783.086577  54.971504  475.315318  761.006527  799.162610  812.285783   910.026830
    Antiques & Collectibles          697.0  783.082124  57.278642  494.586633  759.271158  797.650318  819.108336   928.202725
    Science fiction                  130.0  782.921877  49.009180  572.258923  759.271158  784.303924  806.216143   941.589683
    Law                              895.0  782.768261  58.151503  410.532561  763.039309  800.781298  805.568540   932.478339
    Reference                       1277.0  782.538134  60.935873  174.405146  759.271158  799.162610  812.285783   987.876376
    English fiction                  179.0  780.934686  40.555956  633.724056  763.039309  784.303924  805.568540   873.683536
    Mathematics                     1185.0  779.972390  62.452925  380.492930  763.039309  799.162610  811.867600   914.491840
    Technology & Engineering        1662.0  779.336961  56.934070  306.111983  759.271158  793.504900  805.568540   926.747213
    Travel                          1812.0  778.559368  59.896815  404.940830  755.943132  793.504900  812.285783   936.272603
    Books                            104.0  778.401621  62.306288  514.818623  762.097271  799.162610  805.568540   904.782994
    Political Science               1955.0  776.769388  64.927448  199.515815  762.077591  793.504900  805.568540   930.146793
    Games                            545.0  776.075641  62.866114  447.088904  747.943654  788.471554  811.867600   928.537980
    House & Home                     419.0  775.774113  60.339065  372.523863  746.862879  784.303924  808.508173   919.078743
    Audiobooks                       186.0  775.237246  54.882549  555.562306  747.943654  784.303924  805.568540   904.782994
    Fiction                        23419.0  774.283955  77.453271    0.000000  749.415203  791.455372  819.108336   997.901870
    Large type books                  96.0  771.630674  66.107601  355.742914  763.039309  784.303924  805.568540   902.870823
    Foreign Language Study          1404.0  771.083264  59.376140  433.987638  741.774693  784.303924  805.568540   959.098392
    Games & Activities               446.0  770.363347  69.040492  263.999143  741.774693  784.303924  806.216143   972.154289
    True Crime                       372.0  756.245137  98.184479  132.326345  720.227484  782.208558  809.210980   954.075493
    Computers                       4312.0  754.183606  84.934489  226.875183  719.379707  776.230949  805.568540   953.587344
    Study Aids                       473.0  745.029266  89.049279  288.991248  718.372199  766.908148  805.568540   911.236528


# Linear Regression Analysis of categories


```python
import statsmodels.api as sm
# Converting the labels to one hot encoding
X = pd.get_dummies(data['categories'], drop_first=True,dtype=float)
y = data['Impact']

# Add constant term for the intercept
X = sm.add_constant(X)

# Fit the model
model = sm.OLS(y, X).fit()
```


```python
model.summary()
```




<table class="simpletable">
<caption>OLS Regression Results</caption>
<tr>
  <th>Dep. Variable:</th>         <td>Impact</td>      <th>  R-squared:         </th>  <td>   0.033</td>  
</tr>
<tr>
  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th>  <td>   0.032</td>  
</tr>
<tr>
  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th>  <td>   47.97</td>  
</tr>
<tr>
  <th>Date:</th>             <td>Sat, 10 Aug 2024</td> <th>  Prob (F-statistic):</th>   <td>  0.00</td>   
</tr>
<tr>
  <th>Time:</th>                 <td>14:50:28</td>     <th>  Log-Likelihood:    </th> <td>-7.7066e+05</td>
</tr>
<tr>
  <th>No. Observations:</th>      <td>138724</td>      <th>  AIC:               </th>  <td>1.542e+06</td> 
</tr>
<tr>
  <th>Df Residuals:</th>          <td>138624</td>      <th>  BIC:               </th>  <td>1.543e+06</td> 
</tr>
<tr>
  <th>Df Model:</th>              <td>    99</td>      <th>                     </th>      <td> </td>     
</tr>
<tr>
  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>      <td> </td>     
</tr>
</table>
<table class="simpletable">
<tr>
                <td></td>                   <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>const</th>                         <td>  798.6081</td> <td>    5.668</td> <td>  140.909</td> <td> 0.000</td> <td>  787.500</td> <td>  809.716</td>
</tr>
<tr>
  <th>African Americans</th>             <td>    2.0883</td> <td>    7.301</td> <td>    0.286</td> <td> 0.775</td> <td>  -12.221</td> <td>   16.398</td>
</tr>
<tr>
  <th>American fiction</th>              <td>  -14.7787</td> <td>    7.766</td> <td>   -1.903</td> <td> 0.057</td> <td>  -30.000</td> <td>    0.443</td>
</tr>
<tr>
  <th>American literature</th>           <td>  -12.2032</td> <td>    6.119</td> <td>   -1.994</td> <td> 0.046</td> <td>  -24.196</td> <td>   -0.211</td>
</tr>
<tr>
  <th>American poetry</th>               <td>   -1.2561</td> <td>    7.715</td> <td>   -0.163</td> <td> 0.871</td> <td>  -16.378</td> <td>   13.866</td>
</tr>
<tr>
  <th>Animals</th>                       <td>    7.6475</td> <td>    7.061</td> <td>    1.083</td> <td> 0.279</td> <td>   -6.191</td> <td>   21.486</td>
</tr>
<tr>
  <th>Antiques & Collectibles</th>       <td>  -15.5260</td> <td>    6.144</td> <td>   -2.527</td> <td> 0.011</td> <td>  -27.567</td> <td>   -3.485</td>
</tr>
<tr>
  <th>Architecture</th>                  <td>   -9.2748</td> <td>    6.016</td> <td>   -1.542</td> <td> 0.123</td> <td>  -21.066</td> <td>    2.516</td>
</tr>
<tr>
  <th>Art</th>                           <td>   -3.1646</td> <td>    5.833</td> <td>   -0.542</td> <td> 0.587</td> <td>  -14.598</td> <td>    8.269</td>
</tr>
<tr>
  <th>Audiobooks</th>                    <td>  -23.3709</td> <td>    7.293</td> <td>   -3.205</td> <td> 0.001</td> <td>  -37.665</td> <td>   -9.077</td>
</tr>
<tr>
  <th>Authors</th>                       <td>   -8.1053</td> <td>    8.698</td> <td>   -0.932</td> <td> 0.351</td> <td>  -25.154</td> <td>    8.943</td>
</tr>
<tr>
  <th>Authors, American</th>             <td>  -11.6267</td> <td>    8.291</td> <td>   -1.402</td> <td> 0.161</td> <td>  -27.877</td> <td>    4.624</td>
</tr>
<tr>
  <th>Automobiles</th>                   <td>   -5.5589</td> <td>    9.224</td> <td>   -0.603</td> <td> 0.547</td> <td>  -23.637</td> <td>   12.519</td>
</tr>
<tr>
  <th>Bible</th>                         <td>   -3.7500</td> <td>    6.164</td> <td>   -0.608</td> <td> 0.543</td> <td>  -15.831</td> <td>    8.332</td>
</tr>
<tr>
  <th>Bibles</th>                        <td>    8.9281</td> <td>    6.463</td> <td>    1.381</td> <td> 0.167</td> <td>   -3.740</td> <td>   21.596</td>
</tr>
<tr>
  <th>Biography & Autobiography</th>     <td>  -10.0131</td> <td>    5.722</td> <td>   -1.750</td> <td> 0.080</td> <td>  -21.228</td> <td>    1.202</td>
</tr>
<tr>
  <th>Body, Mind & Spirit</th>           <td>   -4.6971</td> <td>    5.834</td> <td>   -0.805</td> <td> 0.421</td> <td>  -16.131</td> <td>    6.737</td>
</tr>
<tr>
  <th>Books</th>                         <td>  -20.2065</td> <td>    8.355</td> <td>   -2.419</td> <td> 0.016</td> <td>  -36.582</td> <td>   -3.831</td>
</tr>
<tr>
  <th>Brothers and sisters</th>          <td>    2.9510</td> <td>    9.148</td> <td>    0.323</td> <td> 0.747</td> <td>  -14.979</td> <td>   20.881</td>
</tr>
<tr>
  <th>Business & Economics</th>          <td>  -15.1966</td> <td>    5.729</td> <td>   -2.653</td> <td> 0.008</td> <td>  -26.425</td> <td>   -3.969</td>
</tr>
<tr>
  <th>California</th>                    <td>   -7.5896</td> <td>    8.399</td> <td>   -0.904</td> <td> 0.366</td> <td>  -24.051</td> <td>    8.872</td>
</tr>
<tr>
  <th>Canada</th>                        <td>   -0.7761</td> <td>    8.939</td> <td>   -0.087</td> <td> 0.931</td> <td>  -18.297</td> <td>   16.745</td>
</tr>
<tr>
  <th>Cats</th>                          <td>    7.1659</td> <td>    8.421</td> <td>    0.851</td> <td> 0.395</td> <td>   -9.340</td> <td>   23.672</td>
</tr>
<tr>
  <th>Children</th>                      <td>    1.7396</td> <td>    7.951</td> <td>    0.219</td> <td> 0.827</td> <td>  -13.845</td> <td>   17.324</td>
</tr>
<tr>
  <th>Children's literature</th>         <td>    4.1743</td> <td>    8.291</td> <td>    0.503</td> <td> 0.615</td> <td>  -12.076</td> <td>   20.425</td>
</tr>
<tr>
  <th>Children's stories</th>            <td>    5.0433</td> <td>    6.904</td> <td>    0.730</td> <td> 0.465</td> <td>   -8.489</td> <td>   18.576</td>
</tr>
<tr>
  <th>China</th>                         <td>  -11.3175</td> <td>    8.516</td> <td>   -1.329</td> <td> 0.184</td> <td>  -28.009</td> <td>    5.373</td>
</tr>
<tr>
  <th>Christian life</th>                <td>    8.2999</td> <td>    7.151</td> <td>    1.161</td> <td> 0.246</td> <td>   -5.717</td> <td>   22.317</td>
</tr>
<tr>
  <th>Christianity</th>                  <td>   -7.3665</td> <td>    9.040</td> <td>   -0.815</td> <td> 0.415</td> <td>  -25.085</td> <td>   10.352</td>
</tr>
<tr>
  <th>Comic books, strips, etc</th>      <td>   -5.6469</td> <td>    8.492</td> <td>   -0.665</td> <td> 0.506</td> <td>  -22.290</td> <td>   10.997</td>
</tr>
<tr>
  <th>Comics & Graphic Novels</th>       <td>   -8.1050</td> <td>    5.958</td> <td>   -1.360</td> <td> 0.174</td> <td>  -19.782</td> <td>    3.572</td>
</tr>
<tr>
  <th>Computers</th>                     <td>  -44.4245</td> <td>    5.747</td> <td>   -7.730</td> <td> 0.000</td> <td>  -55.689</td> <td>  -33.160</td>
</tr>
<tr>
  <th>Conduct of life</th>               <td>    1.5562</td> <td>    8.154</td> <td>    0.191</td> <td> 0.849</td> <td>  -14.427</td> <td>   17.539</td>
</tr>
<tr>
  <th>Cooking</th>                       <td>    4.1098</td> <td>    5.807</td> <td>    0.708</td> <td> 0.479</td> <td>   -7.272</td> <td>   15.492</td>
</tr>
<tr>
  <th>Copyright</th>                     <td>   -7.8613</td> <td>    7.524</td> <td>   -1.045</td> <td> 0.296</td> <td>  -22.609</td> <td>    6.886</td>
</tr>
<tr>
  <th>Crafts & Hobbies</th>              <td>   -6.3652</td> <td>    5.918</td> <td>   -1.076</td> <td> 0.282</td> <td>  -17.965</td> <td>    5.234</td>
</tr>
<tr>
  <th>Design</th>                        <td>   -8.3250</td> <td>    6.655</td> <td>   -1.251</td> <td> 0.211</td> <td>  -21.369</td> <td>    4.719</td>
</tr>
<tr>
  <th>Detective and mystery stories</th> <td>  -10.6595</td> <td>    6.985</td> <td>   -1.526</td> <td> 0.127</td> <td>  -24.351</td> <td>    3.032</td>
</tr>
<tr>
  <th>Dogs</th>                          <td>    1.0024</td> <td>    8.698</td> <td>    0.115</td> <td> 0.908</td> <td>  -16.046</td> <td>   18.051</td>
</tr>
<tr>
  <th>Drama</th>                         <td>   -8.8261</td> <td>    6.152</td> <td>   -1.435</td> <td> 0.151</td> <td>  -20.883</td> <td>    3.231</td>
</tr>
<tr>
  <th>Education</th>                     <td>   -7.2211</td> <td>    5.798</td> <td>   -1.245</td> <td> 0.213</td> <td>  -18.586</td> <td>    4.144</td>
</tr>
<tr>
  <th>Electronic books</th>              <td>   -3.3535</td> <td>    8.444</td> <td>   -0.397</td> <td> 0.691</td> <td>  -19.904</td> <td>   13.197</td>
</tr>
<tr>
  <th>England</th>                       <td>  -12.6921</td> <td>    8.192</td> <td>   -1.549</td> <td> 0.121</td> <td>  -28.748</td> <td>    3.364</td>
</tr>
<tr>
  <th>English fiction</th>               <td>  -17.6735</td> <td>    7.349</td> <td>   -2.405</td> <td> 0.016</td> <td>  -32.078</td> <td>   -3.269</td>
</tr>
<tr>
  <th>English language</th>              <td>  -14.4038</td> <td>    6.445</td> <td>   -2.235</td> <td> 0.025</td> <td>  -27.036</td> <td>   -1.771</td>
</tr>
<tr>
  <th>English poetry</th>                <td>    1.4342</td> <td>    8.566</td> <td>    0.167</td> <td> 0.867</td> <td>  -15.354</td> <td>   18.223</td>
</tr>
<tr>
  <th>Europe</th>                        <td>   -7.8984</td> <td>    8.844</td> <td>   -0.893</td> <td> 0.372</td> <td>  -25.233</td> <td>    9.437</td>
</tr>
<tr>
  <th>Families</th>                      <td>    4.2153</td> <td>    8.875</td> <td>    0.475</td> <td> 0.635</td> <td>  -13.180</td> <td>   21.611</td>
</tr>
<tr>
  <th>Family & Relationships</th>        <td>   -5.4316</td> <td>    5.824</td> <td>   -0.933</td> <td> 0.351</td> <td>  -16.847</td> <td>    5.983</td>
</tr>
<tr>
  <th>Fiction</th>                       <td>  -24.3242</td> <td>    5.682</td> <td>   -4.281</td> <td> 0.000</td> <td>  -35.461</td> <td>  -13.187</td>
</tr>
<tr>
  <th>Foreign Language Study</th>        <td>  -27.5249</td> <td>    5.909</td> <td>   -4.658</td> <td> 0.000</td> <td>  -39.106</td> <td>  -15.944</td>
</tr>
<tr>
  <th>France</th>                        <td>   -7.8531</td> <td>    8.048</td> <td>   -0.976</td> <td> 0.329</td> <td>  -23.628</td> <td>    7.922</td>
</tr>
<tr>
  <th>Frontier and pioneer life</th>     <td>    3.7800</td> <td>    8.291</td> <td>    0.456</td> <td> 0.648</td> <td>  -12.471</td> <td>   20.031</td>
</tr>
<tr>
  <th>Games</th>                         <td>  -22.5325</td> <td>    6.270</td> <td>   -3.594</td> <td> 0.000</td> <td>  -34.821</td> <td>  -10.244</td>
</tr>
<tr>
  <th>Games & Activities</th>            <td>  -28.2448</td> <td>    6.396</td> <td>   -4.416</td> <td> 0.000</td> <td>  -40.781</td> <td>  -15.709</td>
</tr>
<tr>
  <th>Gardening</th>                     <td>    0.2352</td> <td>    6.284</td> <td>    0.037</td> <td> 0.970</td> <td>  -12.081</td> <td>   12.551</td>
</tr>
<tr>
  <th>Great Britain</th>                 <td>  -10.1787</td> <td>    6.837</td> <td>   -1.489</td> <td> 0.137</td> <td>  -23.579</td> <td>    3.222</td>
</tr>
<tr>
  <th>Health & Fitness</th>              <td>   -5.6597</td> <td>    5.835</td> <td>   -0.970</td> <td> 0.332</td> <td>  -17.097</td> <td>    5.778</td>
</tr>
<tr>
  <th>History</th>                       <td>  -11.4366</td> <td>    5.704</td> <td>   -2.005</td> <td> 0.045</td> <td>  -22.617</td> <td>   -0.256</td>
</tr>
<tr>
  <th>House & Home</th>                  <td>  -22.8340</td> <td>    6.440</td> <td>   -3.546</td> <td> 0.000</td> <td>  -35.456</td> <td>  -10.212</td>
</tr>
<tr>
  <th>Humor</th>                         <td>   -8.7596</td> <td>    6.085</td> <td>   -1.440</td> <td> 0.150</td> <td>  -20.686</td> <td>    3.167</td>
</tr>
<tr>
  <th>Indians of North America</th>      <td>   -5.8180</td> <td>    8.083</td> <td>   -0.720</td> <td> 0.472</td> <td>  -21.660</td> <td>   10.024</td>
</tr>
<tr>
  <th>Jews</th>                          <td>   -1.9266</td> <td>    9.006</td> <td>   -0.214</td> <td> 0.831</td> <td>  -19.578</td> <td>   15.725</td>
</tr>
<tr>
  <th>Juvenile Fiction</th>              <td>    7.9280</td> <td>    5.719</td> <td>    1.386</td> <td> 0.166</td> <td>   -3.282</td> <td>   19.138</td>
</tr>
<tr>
  <th>Juvenile Nonfiction</th>           <td>    0.0246</td> <td>    5.767</td> <td>    0.004</td> <td> 0.997</td> <td>  -11.279</td> <td>   11.328</td>
</tr>
<tr>
  <th>Language Arts & Disciplines</th>   <td>  -10.8597</td> <td>    5.835</td> <td>   -1.861</td> <td> 0.063</td> <td>  -22.296</td> <td>    0.576</td>
</tr>
<tr>
  <th>Large type books</th>              <td>  -26.9775</td> <td>    8.541</td> <td>   -3.159</td> <td> 0.002</td> <td>  -43.717</td> <td>  -10.238</td>
</tr>
<tr>
  <th>Law</th>                           <td>  -15.8399</td> <td>    6.041</td> <td>   -2.622</td> <td> 0.009</td> <td>  -27.681</td> <td>   -3.999</td>
</tr>
<tr>
  <th>Libraries</th>                     <td>   -6.7488</td> <td>    8.671</td> <td>   -0.778</td> <td> 0.436</td> <td>  -23.744</td> <td>   10.246</td>
</tr>
<tr>
  <th>Literary Collections</th>          <td>   -0.6939</td> <td>    6.211</td> <td>   -0.112</td> <td> 0.911</td> <td>  -12.867</td> <td>   11.480</td>
</tr>
<tr>
  <th>Literary Criticism</th>            <td>   -7.3669</td> <td>    5.826</td> <td>   -1.264</td> <td> 0.206</td> <td>  -18.786</td> <td>    4.053</td>
</tr>
<tr>
  <th>Mathematics</th>                   <td>  -18.6358</td> <td>    5.952</td> <td>   -3.131</td> <td> 0.002</td> <td>  -30.302</td> <td>   -6.970</td>
</tr>
<tr>
  <th>Medical</th>                       <td>   -8.1662</td> <td>    5.831</td> <td>   -1.400</td> <td> 0.161</td> <td>  -19.596</td> <td>    3.263</td>
</tr>
<tr>
  <th>Music</th>                         <td>   -9.2514</td> <td>    5.829</td> <td>   -1.587</td> <td> 0.113</td> <td>  -20.677</td> <td>    2.174</td>
</tr>
<tr>
  <th>Nature</th>                        <td>    0.5946</td> <td>    5.962</td> <td>    0.100</td> <td> 0.921</td> <td>  -11.090</td> <td>   12.279</td>
</tr>
<tr>
  <th>Performing Arts</th>               <td>  -11.6704</td> <td>    5.927</td> <td>   -1.969</td> <td> 0.049</td> <td>  -23.286</td> <td>   -0.054</td>
</tr>
<tr>
  <th>Pets</th>                          <td>  -12.8346</td> <td>    6.192</td> <td>   -2.073</td> <td> 0.038</td> <td>  -24.971</td> <td>   -0.698</td>
</tr>
<tr>
  <th>Philosophy</th>                    <td>   -8.1108</td> <td>    5.850</td> <td>   -1.386</td> <td> 0.166</td> <td>  -19.577</td> <td>    3.355</td>
</tr>
<tr>
  <th>Photography</th>                   <td>   -8.0436</td> <td>    6.108</td> <td>   -1.317</td> <td> 0.188</td> <td>  -20.015</td> <td>    3.927</td>
</tr>
<tr>
  <th>Poetry</th>                        <td>    4.9192</td> <td>    5.894</td> <td>    0.835</td> <td> 0.404</td> <td>   -6.632</td> <td>   16.470</td>
</tr>
<tr>
  <th>Political Science</th>             <td>  -21.8388</td> <td>    5.842</td> <td>   -3.738</td> <td> 0.000</td> <td>  -33.288</td> <td>  -10.389</td>
</tr>
<tr>
  <th>Psychology</th>                    <td>   -6.6303</td> <td>    5.845</td> <td>   -1.134</td> <td> 0.257</td> <td>  -18.087</td> <td>    4.827</td>
</tr>
<tr>
  <th>Railroads</th>                     <td>    0.2411</td> <td>    9.075</td> <td>    0.027</td> <td> 0.979</td> <td>  -17.546</td> <td>   18.029</td>
</tr>
<tr>
  <th>Reference</th>                     <td>  -16.0700</td> <td>    5.932</td> <td>   -2.709</td> <td> 0.007</td> <td>  -27.697</td> <td>   -4.443</td>
</tr>
<tr>
  <th>Religion</th>                      <td>    0.4696</td> <td>    5.704</td> <td>    0.082</td> <td> 0.934</td> <td>  -10.710</td> <td>   11.649</td>
</tr>
<tr>
  <th>Science</th>                       <td>  -14.0122</td> <td>    5.798</td> <td>   -2.417</td> <td> 0.016</td> <td>  -25.376</td> <td>   -2.649</td>
</tr>
<tr>
  <th>Science fiction</th>               <td>  -15.6863</td> <td>    7.891</td> <td>   -1.988</td> <td> 0.047</td> <td>  -31.152</td> <td>   -0.220</td>
</tr>
<tr>
  <th>Science fiction, American</th>     <td>  -10.6350</td> <td>    8.939</td> <td>   -1.190</td> <td> 0.234</td> <td>  -28.156</td> <td>    6.886</td>
</tr>
<tr>
  <th>Self-Help</th>                     <td>    3.9991</td> <td>    5.891</td> <td>    0.679</td> <td> 0.497</td> <td>   -7.547</td> <td>   15.545</td>
</tr>
<tr>
  <th>Social Science</th>                <td>  -15.3846</td> <td>    5.757</td> <td>   -2.672</td> <td> 0.008</td> <td>  -26.668</td> <td>   -4.101</td>
</tr>
<tr>
  <th>Sports & Recreation</th>           <td>   -8.1915</td> <td>    5.818</td> <td>   -1.408</td> <td> 0.159</td> <td>  -19.595</td> <td>    3.212</td>
</tr>
<tr>
  <th>Study Aids</th>                    <td>  -53.5789</td> <td>    6.357</td> <td>   -8.429</td> <td> 0.000</td> <td>  -66.038</td> <td>  -41.120</td>
</tr>
<tr>
  <th>Technology & Engineering</th>      <td>  -19.2712</td> <td>    5.872</td> <td>   -3.282</td> <td> 0.001</td> <td>  -30.780</td> <td>   -7.762</td>
</tr>
<tr>
  <th>Transportation</th>                <td>  -15.5216</td> <td>    6.031</td> <td>   -2.574</td> <td> 0.010</td> <td>  -27.343</td> <td>   -3.700</td>
</tr>
<tr>
  <th>Travel</th>                        <td>  -20.0488</td> <td>    5.855</td> <td>   -3.424</td> <td> 0.001</td> <td>  -31.525</td> <td>   -8.573</td>
</tr>
<tr>
  <th>True Crime</th>                    <td>  -42.3630</td> <td>    6.531</td> <td>   -6.486</td> <td> 0.000</td> <td>  -55.164</td> <td>  -29.562</td>
</tr>
<tr>
  <th>United States</th>                 <td>  -10.6347</td> <td>    6.500</td> <td>   -1.636</td> <td> 0.102</td> <td>  -23.374</td> <td>    2.105</td>
</tr>
<tr>
  <th>World War, 1939-1945</th>          <td>   -6.1006</td> <td>    7.317</td> <td>   -0.834</td> <td> 0.404</td> <td>  -20.441</td> <td>    8.240</td>
</tr>
<tr>
  <th>Young Adult Fiction</th>           <td>  -15.4470</td> <td>    6.221</td> <td>   -2.483</td> <td> 0.013</td> <td>  -27.641</td> <td>   -3.253</td>
</tr>
<tr>
  <th>Young Adult Nonfiction</th>        <td>   13.6191</td> <td>    9.040</td> <td>    1.506</td> <td> 0.132</td> <td>   -4.100</td> <td>   31.338</td>
</tr>
</table>
<table class="simpletable">
<tr>
  <th>Omnibus:</th>       <td>62893.860</td> <th>  Durbin-Watson:     </th>  <td>   1.996</td> 
</tr>
<tr>
  <th>Prob(Omnibus):</th>  <td> 0.000</td>   <th>  Jarque-Bera (JB):  </th> <td>570375.112</td>
</tr>
<tr>
  <th>Skew:</th>           <td>-1.965</td>   <th>  Prob(JB):          </th>  <td>    0.00</td> 
</tr>
<tr>
  <th>Kurtosis:</th>       <td>12.123</td>   <th>  Cond. No.          </th>  <td>    347.</td> 
</tr>
</table><br/><br/>Notes:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.



## Summary of the analysis:
1. The R-squared value indicates that the model explains only 3.3% of the variance in the dependent variable.
2. const (Intercept): 798.6081
       <t>The expected value of the Impact when all predictor variables are zero.</t>
3. African Americans: 2.0883 (p-value: 0.775)
       The coefficient for African Americans is not statistically significant (p > 0.05). This suggests that African Americans might not          have a significant effect on Impact given the other variables in the model.
4. American fiction: -14.7787 (p-value: 0.057)
       The coefficient is negative and close to the 0.05 significance threshold. This implies that American fiction might have a negative         effect on Impact, but the result is not highly significant.
5. American literature: -12.2032 (p-value: 0.046)
       This coefficient is negative and statistically significant (p < 0.05), suggesting that American literature has a significant               negative effect on Impact.

## Re-running linear analysis on categories with frequency encoding


```python
# Calculate frequencies
frequency = data['categories'].value_counts()

# Define a threshold for rare categories
threshold = 10

# Group rare categories into 'Other'
data['Category'] = data['categories'].apply(lambda x: x if frequency[x] > threshold else 'Other')

# Recalculate frequencies after grouping
frequency = data['Category'].value_counts()

# Map frequencies to the DataFrame
data['Category_freq'] = data['Category'].map(frequency)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data['Category_freq'] = scaler.fit_transform(data[['Category_freq']])
```


```python
import statsmodels.api as sm
X = data['Category_freq']
print(X.head())
y = data['Impact']

# Add constant term for the intercept
X = sm.add_constant(X)

# Fit the model
model = sm.OLS(y, X).fit()
```

    0   -0.758377
    1   -0.101394
    2    0.297607
    3    2.074339
    4    0.297607
    Name: Category_freq, dtype: float64



```python
model.summary()
```




<table class="simpletable">
<caption>OLS Regression Results</caption>
<tr>
  <th>Dep. Variable:</th>         <td>Impact</td>      <th>  R-squared:         </th>  <td>   0.005</td>  
</tr>
<tr>
  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th>  <td>   0.005</td>  
</tr>
<tr>
  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th>  <td>   747.3</td>  
</tr>
<tr>
  <th>Date:</th>             <td>Sat, 10 Aug 2024</td> <th>  Prob (F-statistic):</th>  <td>4.15e-164</td> 
</tr>
<tr>
  <th>Time:</th>                 <td>15:40:35</td>     <th>  Log-Likelihood:    </th> <td>-7.7262e+05</td>
</tr>
<tr>
  <th>No. Observations:</th>      <td>138724</td>      <th>  AIC:               </th>  <td>1.545e+06</td> 
</tr>
<tr>
  <th>Df Residuals:</th>          <td>138722</td>      <th>  BIC:               </th>  <td>1.545e+06</td> 
</tr>
<tr>
  <th>Df Model:</th>              <td>     1</td>      <th>                     </th>      <td> </td>     
</tr>
<tr>
  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>      <td> </td>     
</tr>
</table>
<table class="simpletable">
<tr>
        <td></td>           <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>const</th>         <td>  786.7637</td> <td>    0.170</td> <td> 4616.923</td> <td> 0.000</td> <td>  786.430</td> <td>  787.098</td>
</tr>
<tr>
  <th>Category_freq</th> <td>   -4.6586</td> <td>    0.170</td> <td>  -27.338</td> <td> 0.000</td> <td>   -4.993</td> <td>   -4.325</td>
</tr>
</table>
<table class="simpletable">
<tr>
  <th>Omnibus:</th>       <td>63085.097</td> <th>  Durbin-Watson:     </th>  <td>   1.997</td> 
</tr>
<tr>
  <th>Prob(Omnibus):</th>  <td> 0.000</td>   <th>  Jarque-Bera (JB):  </th> <td>564492.440</td>
</tr>
<tr>
  <th>Skew:</th>           <td>-1.978</td>   <th>  Prob(JB):          </th>  <td>    0.00</td> 
</tr>
<tr>
  <th>Kurtosis:</th>       <td>12.056</td>   <th>  Cond. No.          </th>  <td>    1.00</td> 
</tr>
</table><br/><br/>Notes:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.



## Summary of the analysis
1. R-squared of 0.005 suggests that the model explains only 0.5% of the variance in the dependent variable (Impact). This indicates that the model does not fit the data well.
2. Both the intercept and Category_freq are statistically significant (p-value < 0.05). This suggests that Category_freq has a meaningful relationship with Impact, even though the overall model has low explanatory power.

# Investigating relationship of publisher on Impact


```python
print(data.groupby('publisher').describe()['Impact'].sort_values('mean').head(100).to_string())
```

                                          count        mean         std         min         25%         50%         75%         max
    publisher                                                                                                                      
    Sentinel                                1.0  199.515815         NaN  199.515815  199.515815  199.515815  199.515815  199.515815
    Anita Blake, Vampire Hunter             1.0  215.427496         NaN  215.427496  215.427496  215.427496  215.427496  215.427496
    Shady Creek Publishing                  1.0  290.116156         NaN  290.116156  290.116156  290.116156  290.116156  290.116156
    Blood Moon Productions, Ltd.            1.0  290.747321         NaN  290.747321  290.747321  290.747321  290.747321  290.747321
    Adv Films                               1.0  307.629607         NaN  307.629607  307.629607  307.629607  307.629607  307.629607
    Book Factory                            1.0  335.908895         NaN  335.908895  335.908895  335.908895  335.908895  335.908895
    Holly Hall Pub                          1.0  351.633127         NaN  351.633127  351.633127  351.633127  351.633127  351.633127
    Bell                                    1.0  359.888695         NaN  359.888695  359.888695  359.888695  359.888695  359.888695
    Cooper Square Press                     1.0  380.526035         NaN  380.526035  380.526035  380.526035  380.526035  380.526035
    Jeffries Publishing                     1.0  414.438216         NaN  414.438216  414.438216  414.438216  414.438216  414.438216
    Family Station Incorporated             1.0  422.008033         NaN  422.008033  422.008033  422.008033  422.008033  422.008033
    Quick Reference Guides (Harves          1.0  442.489404         NaN  442.489404  442.489404  442.489404  442.489404  442.489404
    Ginka Opalchenova                       1.0  446.038745         NaN  446.038745  446.038745  446.038745  446.038745  446.038745
    Darwin's Radio                          1.0  450.165845         NaN  450.165845  450.165845  450.165845  450.165845  450.165845
    The Interpreter Foundation              1.0  458.176067         NaN  458.176067  458.176067  458.176067  458.176067  458.176067
    RP Minis                                1.0  465.329838         NaN  465.329838  465.329838  465.329838  465.329838  465.329838
    Rowohlt Verlag GmbH                     1.0  468.261587         NaN  468.261587  468.261587  468.261587  468.261587  468.261587
    Axicon Circle, LLC                      1.0  474.573141         NaN  474.573141  474.573141  474.573141  474.573141  474.573141
    Logical Figments Incorporated           1.0  474.929762         NaN  474.929762  474.929762  474.929762  474.929762  474.929762
    Gallery                                 1.0  479.794397         NaN  479.794397  479.794397  479.794397  479.794397  479.794397
    Grover E. Murray Studies in th          1.0  480.015206         NaN  480.015206  480.015206  480.015206  480.015206  480.015206
    BOOM! Studios                           1.0  480.398525         NaN  480.398525  480.398525  480.398525  480.398525  480.398525
    Techni Visions Llc                      1.0  484.178482         NaN  484.178482  484.178482  484.178482  484.178482  484.178482
    Resurrection House                      1.0  487.486789         NaN  487.486789  487.486789  487.486789  487.486789  487.486789
    Enlightened Financial Press             2.0  488.731298  137.983975  391.161893  439.946595  488.731298  537.516000  586.300702
    Wildblue Press                          1.0  488.766649         NaN  488.766649  488.766649  488.766649  488.766649  488.766649
    Promtheus                               1.0  490.388253         NaN  490.388253  490.388253  490.388253  490.388253  490.388253
    The-End.Com Incorporated                1.0  514.059279         NaN  514.059279  514.059279  514.059279  514.059279  514.059279
    Ashleywilde, Inc.                       1.0  517.856252         NaN  517.856252  517.856252  517.856252  517.856252  517.856252
    Greenwood Press                         1.0  525.772148         NaN  525.772148  525.772148  525.772148  525.772148  525.772148
    Kids of North Jersey Nurses             1.0  525.772148         NaN  525.772148  525.772148  525.772148  525.772148  525.772148
    Julia London                            1.0  526.137991         NaN  526.137991  526.137991  526.137991  526.137991  526.137991
    First Biltmore Corporation              1.0  527.012252         NaN  527.012252  527.012252  527.012252  527.012252  527.012252
    Mr Roy Heaps                            1.0  528.179093         NaN  528.179093  528.179093  528.179093  528.179093  528.179093
    Momentum Books Llc                      1.0  531.300093         NaN  531.300093  531.300093  531.300093  531.300093  531.300093
    Silicon Pr                              1.0  532.640187         NaN  532.640187  532.640187  532.640187  532.640187  532.640187
    Midwest Christian Outreach              1.0  533.116545         NaN  533.116545  533.116545  533.116545  533.116545  533.116545
    Creation Liberty Evangelism             1.0  534.049437         NaN  534.049437  534.049437  534.049437  534.049437  534.049437
    Jenrod Incorporated                     1.0  534.598189         NaN  534.598189  534.598189  534.598189  534.598189  534.598189
    Transitions Abroad Pub                  1.0  540.406480         NaN  540.406480  540.406480  540.406480  540.406480  540.406480
    Julian Dibbell                          1.0  540.804887         NaN  540.804887  540.804887  540.804887  540.804887  540.804887
    Woodstocck, N.Y. : Overlook Press       1.0  546.113908         NaN  546.113908  546.113908  546.113908  546.113908  546.113908
    Time Out LLC                            1.0  546.994284         NaN  546.994284  546.994284  546.994284  546.994284  546.994284
    Newbury House                           1.0  547.864610         NaN  547.864610  547.864610  547.864610  547.864610  547.864610
    FLEXquarters.com Limited                2.0  548.804671   58.659574  507.326088  528.065379  548.804671  569.543962  590.283253
    Information USA Incorporated            5.0  551.103668  258.848903  174.405146  426.210996  612.989675  700.207202  841.705321
    Nash Pub                                1.0  551.298335         NaN  551.298335  551.298335  551.298335  551.298335  551.298335
    Mark Dice                               1.0  552.648719         NaN  552.648719  552.648719  552.648719  552.648719  552.648719
    Rockpress Publishing Company            1.0  553.737562         NaN  553.737562  553.737562  553.737562  553.737562  553.737562
    Winding Star Press                      1.0  556.149605         NaN  556.149605  556.149605  556.149605  556.149605  556.149605
    Gambling Research Institute             1.0  556.171815         NaN  556.171815  556.171815  556.171815  556.171815  556.171815
    GCB Publishing Group                    1.0  563.636251         NaN  563.636251  563.636251  563.636251  563.636251  563.636251
    Admission Test Passbooks                1.0  565.347834         NaN  565.347834  565.347834  565.347834  565.347834  565.347834
    Western Front Limited                   1.0  565.855478         NaN  565.855478  565.855478  565.855478  565.855478  565.855478
    Dinah Dinwiddie                         1.0  568.997382         NaN  568.997382  568.997382  568.997382  568.997382  568.997382
    Lichén via PublishDrive                 1.0  570.709918         NaN  570.709918  570.709918  570.709918  570.709918  570.709918
    Xamonline                               1.0  572.152802         NaN  572.152802  572.152802  572.152802  572.152802  572.152802
    Odyssey Books                           1.0  574.442878         NaN  574.442878  574.442878  574.442878  574.442878  574.442878
    B S Book Pub                            2.0  574.815574  151.587352  467.627130  521.221352  574.815574  628.409796  682.004019
    Pocket Star                             3.0  575.521091   81.866120  484.634257  541.543838  598.453420  620.964509  643.475597
    Brunswick Publishing Company            3.0  577.411124  237.287063  337.783079  459.973794  582.164510  697.225147  812.285783
    Justin Kelly                            1.0  580.019707         NaN  580.019707  580.019707  580.019707  580.019707  580.019707
    Chilton total car care                  1.0  582.024487         NaN  582.024487  582.024487  582.024487  582.024487  582.024487
    Thurman House Llc                       1.0  582.164510         NaN  582.164510  582.164510  582.164510  582.164510  582.164510
    Ace Academics Inc.                      1.0  582.164510         NaN  582.164510  582.164510  582.164510  582.164510  582.164510
    Pearson South Africa                    1.0  582.164510         NaN  582.164510  582.164510  582.164510  582.164510  582.164510
    Lb Books                                1.0  583.917166         NaN  583.917166  583.917166  583.917166  583.917166  583.917166
    Two Plus Two Pub                        1.0  584.771461         NaN  584.771461  584.771461  584.771461  584.771461  584.771461
    Station Hill Press                      1.0  585.251245         NaN  585.251245  585.251245  585.251245  585.251245  585.251245
    Tantor Media, Incorporated              1.0  587.147842         NaN  587.147842  587.147842  587.147842  587.147842  587.147842
    A Nick Hoffman / Academic Mystery       1.0  587.725696         NaN  587.725696  587.725696  587.725696  587.725696  587.725696
    Marathon International Book Company     2.0  588.007745  158.025443  476.266883  532.137314  588.007745  643.878176  699.748608
    Aarhus Universitetsforlag               1.0  588.133788         NaN  588.133788  588.133788  588.133788  588.133788  588.133788
    Imported Publication                    1.0  590.732088         NaN  590.732088  590.732088  590.732088  590.732088  590.732088
    Rswinc                                  1.0  591.417839         NaN  591.417839  591.417839  591.417839  591.417839  591.417839
    Big Mac Publishers                      1.0  591.917088         NaN  591.917088  591.917088  591.917088  591.917088  591.917088
    Bookhaus                                1.0  593.281073         NaN  593.281073  593.281073  593.281073  593.281073  593.281073
    Danielle Ward Do                        1.0  593.537878         NaN  593.537878  593.537878  593.537878  593.537878  593.537878
    Enlightened Publishing                  1.0  593.537878         NaN  593.537878  593.537878  593.537878  593.537878  593.537878
    Milo House Press                        1.0  593.537878         NaN  593.537878  593.537878  593.537878  593.537878  593.537878
    Warren Press                           14.0  593.662102    0.285260  593.281073  593.537878  593.634343  593.843498  594.099915
    Cad/Cam Pub                             1.0  593.730809         NaN  593.730809  593.730809  593.730809  593.730809  593.730809
    Star Trek                               6.0  595.812500  190.447752  368.235929  445.277724  593.352101  732.172168  845.569747
    Living Truth Pub                        4.0  596.866414   27.332720  558.311338  587.879596  604.380672  613.367490  620.392973
    Marian Wood Books/Putnam                1.0  596.888299         NaN  596.888299  596.888299  596.888299  596.888299  596.888299
    Mary Russell & Sherlock Holmes          1.0  597.060757         NaN  597.060757  597.060757  597.060757  597.060757  597.060757
    Black Dog Publishing                    1.0  597.270348         NaN  597.270348  597.270348  597.270348  597.270348  597.270348
    Goodale Pubs                            1.0  598.051697         NaN  598.051697  598.051697  598.051697  598.051697  598.051697
    Ballou Press                            1.0  598.051697         NaN  598.051697  598.051697  598.051697  598.051697  598.051697
    Hourglass                               1.0  598.453420         NaN  598.453420  598.453420  598.453420  598.453420  598.453420
    Amer Group Pub                          1.0  598.981186         NaN  598.981186  598.981186  598.981186  598.981186  598.981186
    Adonis Ed                               1.0  598.981186         NaN  598.981186  598.981186  598.981186  598.981186  598.981186
    Classical Comics                        1.0  598.981186         NaN  598.981186  598.981186  598.981186  598.981186  598.981186
    Tor Fantasy                             6.0  599.583460  302.041333    0.000000  619.497043  727.994470  755.505382  793.504900
    New Falcon Publications                 1.0  600.260249         NaN  600.260249  600.260249  600.260249  600.260249  600.260249
    Western Front                           1.0  600.260249         NaN  600.260249  600.260249  600.260249  600.260249  600.260249
    Fountain of Youth Group Incorporated    1.0  600.260249         NaN  600.260249  600.260249  600.260249  600.260249  600.260249
    Mike Cortson Company USA                1.0  602.041776         NaN  602.041776  602.041776  602.041776  602.041776  602.041776
    Thorndike Press Large Print             3.0  602.172520  185.871171  444.540707  499.692682  554.844657  680.988427  807.132198
    Wickosity Media, LLC                    1.0  603.808761         NaN  603.808761  603.808761  603.808761  603.808761  603.808761



```python
import statsmodels.api as sm
# Calculate frequencies
frequency = data['publisher'].value_counts()

# Define a threshold for rare categories
threshold = 20

# Group rare categories into 'Other'
data['publisher'] = data['publisher'].apply(lambda x: x if frequency[x] > threshold else 'Other')

# Converting the labels to one hot encoding
X = pd.get_dummies(data['categories'], drop_first=True,dtype=float)
y = data['Impact']

# Add constant term for the intercept
X = sm.add_constant(X)

# Fit the model
model = sm.OLS(y, X).fit()
```


```python
data['publisher'].value_counts()
```




    publisher
    Other                                       32945
    Tan Books & Pub                              3635
    Simon and Schuster                           3600
    Smithsonian Institution                      3216
    Penguin                                      2788
                                                ...  
    Flatiron Books                                 21
    Boydell & Brewer                               21
    Disney-Hyperion                                21
    Simon & Schuster Books For Young Readers       21
    Rough Guides                                   21
    Name: count, Length: 898, dtype: int64




```python
model.summary()
```




<table class="simpletable">
<caption>OLS Regression Results</caption>
<tr>
  <th>Dep. Variable:</th>         <td>Impact</td>      <th>  R-squared:         </th>  <td>   0.033</td>  
</tr>
<tr>
  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th>  <td>   0.032</td>  
</tr>
<tr>
  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th>  <td>   47.97</td>  
</tr>
<tr>
  <th>Date:</th>             <td>Sat, 10 Aug 2024</td> <th>  Prob (F-statistic):</th>   <td>  0.00</td>   
</tr>
<tr>
  <th>Time:</th>                 <td>16:09:30</td>     <th>  Log-Likelihood:    </th> <td>-7.7066e+05</td>
</tr>
<tr>
  <th>No. Observations:</th>      <td>138724</td>      <th>  AIC:               </th>  <td>1.542e+06</td> 
</tr>
<tr>
  <th>Df Residuals:</th>          <td>138624</td>      <th>  BIC:               </th>  <td>1.543e+06</td> 
</tr>
<tr>
  <th>Df Model:</th>              <td>    99</td>      <th>                     </th>      <td> </td>     
</tr>
<tr>
  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>      <td> </td>     
</tr>
</table>
<table class="simpletable">
<tr>
                <td></td>                   <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>const</th>                         <td>  798.6081</td> <td>    5.668</td> <td>  140.909</td> <td> 0.000</td> <td>  787.500</td> <td>  809.716</td>
</tr>
<tr>
  <th>African Americans</th>             <td>    2.0883</td> <td>    7.301</td> <td>    0.286</td> <td> 0.775</td> <td>  -12.221</td> <td>   16.398</td>
</tr>
<tr>
  <th>American fiction</th>              <td>  -14.7787</td> <td>    7.766</td> <td>   -1.903</td> <td> 0.057</td> <td>  -30.000</td> <td>    0.443</td>
</tr>
<tr>
  <th>American literature</th>           <td>  -12.2032</td> <td>    6.119</td> <td>   -1.994</td> <td> 0.046</td> <td>  -24.196</td> <td>   -0.211</td>
</tr>
<tr>
  <th>American poetry</th>               <td>   -1.2561</td> <td>    7.715</td> <td>   -0.163</td> <td> 0.871</td> <td>  -16.378</td> <td>   13.866</td>
</tr>
<tr>
  <th>Animals</th>                       <td>    7.6475</td> <td>    7.061</td> <td>    1.083</td> <td> 0.279</td> <td>   -6.191</td> <td>   21.486</td>
</tr>
<tr>
  <th>Antiques & Collectibles</th>       <td>  -15.5260</td> <td>    6.144</td> <td>   -2.527</td> <td> 0.011</td> <td>  -27.567</td> <td>   -3.485</td>
</tr>
<tr>
  <th>Architecture</th>                  <td>   -9.2748</td> <td>    6.016</td> <td>   -1.542</td> <td> 0.123</td> <td>  -21.066</td> <td>    2.516</td>
</tr>
<tr>
  <th>Art</th>                           <td>   -3.1646</td> <td>    5.833</td> <td>   -0.542</td> <td> 0.587</td> <td>  -14.598</td> <td>    8.269</td>
</tr>
<tr>
  <th>Audiobooks</th>                    <td>  -23.3709</td> <td>    7.293</td> <td>   -3.205</td> <td> 0.001</td> <td>  -37.665</td> <td>   -9.077</td>
</tr>
<tr>
  <th>Authors</th>                       <td>   -8.1053</td> <td>    8.698</td> <td>   -0.932</td> <td> 0.351</td> <td>  -25.154</td> <td>    8.943</td>
</tr>
<tr>
  <th>Authors, American</th>             <td>  -11.6267</td> <td>    8.291</td> <td>   -1.402</td> <td> 0.161</td> <td>  -27.877</td> <td>    4.624</td>
</tr>
<tr>
  <th>Automobiles</th>                   <td>   -5.5589</td> <td>    9.224</td> <td>   -0.603</td> <td> 0.547</td> <td>  -23.637</td> <td>   12.519</td>
</tr>
<tr>
  <th>Bible</th>                         <td>   -3.7500</td> <td>    6.164</td> <td>   -0.608</td> <td> 0.543</td> <td>  -15.831</td> <td>    8.332</td>
</tr>
<tr>
  <th>Bibles</th>                        <td>    8.9281</td> <td>    6.463</td> <td>    1.381</td> <td> 0.167</td> <td>   -3.740</td> <td>   21.596</td>
</tr>
<tr>
  <th>Biography & Autobiography</th>     <td>  -10.0131</td> <td>    5.722</td> <td>   -1.750</td> <td> 0.080</td> <td>  -21.228</td> <td>    1.202</td>
</tr>
<tr>
  <th>Body, Mind & Spirit</th>           <td>   -4.6971</td> <td>    5.834</td> <td>   -0.805</td> <td> 0.421</td> <td>  -16.131</td> <td>    6.737</td>
</tr>
<tr>
  <th>Books</th>                         <td>  -20.2065</td> <td>    8.355</td> <td>   -2.419</td> <td> 0.016</td> <td>  -36.582</td> <td>   -3.831</td>
</tr>
<tr>
  <th>Brothers and sisters</th>          <td>    2.9510</td> <td>    9.148</td> <td>    0.323</td> <td> 0.747</td> <td>  -14.979</td> <td>   20.881</td>
</tr>
<tr>
  <th>Business & Economics</th>          <td>  -15.1966</td> <td>    5.729</td> <td>   -2.653</td> <td> 0.008</td> <td>  -26.425</td> <td>   -3.969</td>
</tr>
<tr>
  <th>California</th>                    <td>   -7.5896</td> <td>    8.399</td> <td>   -0.904</td> <td> 0.366</td> <td>  -24.051</td> <td>    8.872</td>
</tr>
<tr>
  <th>Canada</th>                        <td>   -0.7761</td> <td>    8.939</td> <td>   -0.087</td> <td> 0.931</td> <td>  -18.297</td> <td>   16.745</td>
</tr>
<tr>
  <th>Cats</th>                          <td>    7.1659</td> <td>    8.421</td> <td>    0.851</td> <td> 0.395</td> <td>   -9.340</td> <td>   23.672</td>
</tr>
<tr>
  <th>Children</th>                      <td>    1.7396</td> <td>    7.951</td> <td>    0.219</td> <td> 0.827</td> <td>  -13.845</td> <td>   17.324</td>
</tr>
<tr>
  <th>Children's literature</th>         <td>    4.1743</td> <td>    8.291</td> <td>    0.503</td> <td> 0.615</td> <td>  -12.076</td> <td>   20.425</td>
</tr>
<tr>
  <th>Children's stories</th>            <td>    5.0433</td> <td>    6.904</td> <td>    0.730</td> <td> 0.465</td> <td>   -8.489</td> <td>   18.576</td>
</tr>
<tr>
  <th>China</th>                         <td>  -11.3175</td> <td>    8.516</td> <td>   -1.329</td> <td> 0.184</td> <td>  -28.009</td> <td>    5.373</td>
</tr>
<tr>
  <th>Christian life</th>                <td>    8.2999</td> <td>    7.151</td> <td>    1.161</td> <td> 0.246</td> <td>   -5.717</td> <td>   22.317</td>
</tr>
<tr>
  <th>Christianity</th>                  <td>   -7.3665</td> <td>    9.040</td> <td>   -0.815</td> <td> 0.415</td> <td>  -25.085</td> <td>   10.352</td>
</tr>
<tr>
  <th>Comic books, strips, etc</th>      <td>   -5.6469</td> <td>    8.492</td> <td>   -0.665</td> <td> 0.506</td> <td>  -22.290</td> <td>   10.997</td>
</tr>
<tr>
  <th>Comics & Graphic Novels</th>       <td>   -8.1050</td> <td>    5.958</td> <td>   -1.360</td> <td> 0.174</td> <td>  -19.782</td> <td>    3.572</td>
</tr>
<tr>
  <th>Computers</th>                     <td>  -44.4245</td> <td>    5.747</td> <td>   -7.730</td> <td> 0.000</td> <td>  -55.689</td> <td>  -33.160</td>
</tr>
<tr>
  <th>Conduct of life</th>               <td>    1.5562</td> <td>    8.154</td> <td>    0.191</td> <td> 0.849</td> <td>  -14.427</td> <td>   17.539</td>
</tr>
<tr>
  <th>Cooking</th>                       <td>    4.1098</td> <td>    5.807</td> <td>    0.708</td> <td> 0.479</td> <td>   -7.272</td> <td>   15.492</td>
</tr>
<tr>
  <th>Copyright</th>                     <td>   -7.8613</td> <td>    7.524</td> <td>   -1.045</td> <td> 0.296</td> <td>  -22.609</td> <td>    6.886</td>
</tr>
<tr>
  <th>Crafts & Hobbies</th>              <td>   -6.3652</td> <td>    5.918</td> <td>   -1.076</td> <td> 0.282</td> <td>  -17.965</td> <td>    5.234</td>
</tr>
<tr>
  <th>Design</th>                        <td>   -8.3250</td> <td>    6.655</td> <td>   -1.251</td> <td> 0.211</td> <td>  -21.369</td> <td>    4.719</td>
</tr>
<tr>
  <th>Detective and mystery stories</th> <td>  -10.6595</td> <td>    6.985</td> <td>   -1.526</td> <td> 0.127</td> <td>  -24.351</td> <td>    3.032</td>
</tr>
<tr>
  <th>Dogs</th>                          <td>    1.0024</td> <td>    8.698</td> <td>    0.115</td> <td> 0.908</td> <td>  -16.046</td> <td>   18.051</td>
</tr>
<tr>
  <th>Drama</th>                         <td>   -8.8261</td> <td>    6.152</td> <td>   -1.435</td> <td> 0.151</td> <td>  -20.883</td> <td>    3.231</td>
</tr>
<tr>
  <th>Education</th>                     <td>   -7.2211</td> <td>    5.798</td> <td>   -1.245</td> <td> 0.213</td> <td>  -18.586</td> <td>    4.144</td>
</tr>
<tr>
  <th>Electronic books</th>              <td>   -3.3535</td> <td>    8.444</td> <td>   -0.397</td> <td> 0.691</td> <td>  -19.904</td> <td>   13.197</td>
</tr>
<tr>
  <th>England</th>                       <td>  -12.6921</td> <td>    8.192</td> <td>   -1.549</td> <td> 0.121</td> <td>  -28.748</td> <td>    3.364</td>
</tr>
<tr>
  <th>English fiction</th>               <td>  -17.6735</td> <td>    7.349</td> <td>   -2.405</td> <td> 0.016</td> <td>  -32.078</td> <td>   -3.269</td>
</tr>
<tr>
  <th>English language</th>              <td>  -14.4038</td> <td>    6.445</td> <td>   -2.235</td> <td> 0.025</td> <td>  -27.036</td> <td>   -1.771</td>
</tr>
<tr>
  <th>English poetry</th>                <td>    1.4342</td> <td>    8.566</td> <td>    0.167</td> <td> 0.867</td> <td>  -15.354</td> <td>   18.223</td>
</tr>
<tr>
  <th>Europe</th>                        <td>   -7.8984</td> <td>    8.844</td> <td>   -0.893</td> <td> 0.372</td> <td>  -25.233</td> <td>    9.437</td>
</tr>
<tr>
  <th>Families</th>                      <td>    4.2153</td> <td>    8.875</td> <td>    0.475</td> <td> 0.635</td> <td>  -13.180</td> <td>   21.611</td>
</tr>
<tr>
  <th>Family & Relationships</th>        <td>   -5.4316</td> <td>    5.824</td> <td>   -0.933</td> <td> 0.351</td> <td>  -16.847</td> <td>    5.983</td>
</tr>
<tr>
  <th>Fiction</th>                       <td>  -24.3242</td> <td>    5.682</td> <td>   -4.281</td> <td> 0.000</td> <td>  -35.461</td> <td>  -13.187</td>
</tr>
<tr>
  <th>Foreign Language Study</th>        <td>  -27.5249</td> <td>    5.909</td> <td>   -4.658</td> <td> 0.000</td> <td>  -39.106</td> <td>  -15.944</td>
</tr>
<tr>
  <th>France</th>                        <td>   -7.8531</td> <td>    8.048</td> <td>   -0.976</td> <td> 0.329</td> <td>  -23.628</td> <td>    7.922</td>
</tr>
<tr>
  <th>Frontier and pioneer life</th>     <td>    3.7800</td> <td>    8.291</td> <td>    0.456</td> <td> 0.648</td> <td>  -12.471</td> <td>   20.031</td>
</tr>
<tr>
  <th>Games</th>                         <td>  -22.5325</td> <td>    6.270</td> <td>   -3.594</td> <td> 0.000</td> <td>  -34.821</td> <td>  -10.244</td>
</tr>
<tr>
  <th>Games & Activities</th>            <td>  -28.2448</td> <td>    6.396</td> <td>   -4.416</td> <td> 0.000</td> <td>  -40.781</td> <td>  -15.709</td>
</tr>
<tr>
  <th>Gardening</th>                     <td>    0.2352</td> <td>    6.284</td> <td>    0.037</td> <td> 0.970</td> <td>  -12.081</td> <td>   12.551</td>
</tr>
<tr>
  <th>Great Britain</th>                 <td>  -10.1787</td> <td>    6.837</td> <td>   -1.489</td> <td> 0.137</td> <td>  -23.579</td> <td>    3.222</td>
</tr>
<tr>
  <th>Health & Fitness</th>              <td>   -5.6597</td> <td>    5.835</td> <td>   -0.970</td> <td> 0.332</td> <td>  -17.097</td> <td>    5.778</td>
</tr>
<tr>
  <th>History</th>                       <td>  -11.4366</td> <td>    5.704</td> <td>   -2.005</td> <td> 0.045</td> <td>  -22.617</td> <td>   -0.256</td>
</tr>
<tr>
  <th>House & Home</th>                  <td>  -22.8340</td> <td>    6.440</td> <td>   -3.546</td> <td> 0.000</td> <td>  -35.456</td> <td>  -10.212</td>
</tr>
<tr>
  <th>Humor</th>                         <td>   -8.7596</td> <td>    6.085</td> <td>   -1.440</td> <td> 0.150</td> <td>  -20.686</td> <td>    3.167</td>
</tr>
<tr>
  <th>Indians of North America</th>      <td>   -5.8180</td> <td>    8.083</td> <td>   -0.720</td> <td> 0.472</td> <td>  -21.660</td> <td>   10.024</td>
</tr>
<tr>
  <th>Jews</th>                          <td>   -1.9266</td> <td>    9.006</td> <td>   -0.214</td> <td> 0.831</td> <td>  -19.578</td> <td>   15.725</td>
</tr>
<tr>
  <th>Juvenile Fiction</th>              <td>    7.9280</td> <td>    5.719</td> <td>    1.386</td> <td> 0.166</td> <td>   -3.282</td> <td>   19.138</td>
</tr>
<tr>
  <th>Juvenile Nonfiction</th>           <td>    0.0246</td> <td>    5.767</td> <td>    0.004</td> <td> 0.997</td> <td>  -11.279</td> <td>   11.328</td>
</tr>
<tr>
  <th>Language Arts & Disciplines</th>   <td>  -10.8597</td> <td>    5.835</td> <td>   -1.861</td> <td> 0.063</td> <td>  -22.296</td> <td>    0.576</td>
</tr>
<tr>
  <th>Large type books</th>              <td>  -26.9775</td> <td>    8.541</td> <td>   -3.159</td> <td> 0.002</td> <td>  -43.717</td> <td>  -10.238</td>
</tr>
<tr>
  <th>Law</th>                           <td>  -15.8399</td> <td>    6.041</td> <td>   -2.622</td> <td> 0.009</td> <td>  -27.681</td> <td>   -3.999</td>
</tr>
<tr>
  <th>Libraries</th>                     <td>   -6.7488</td> <td>    8.671</td> <td>   -0.778</td> <td> 0.436</td> <td>  -23.744</td> <td>   10.246</td>
</tr>
<tr>
  <th>Literary Collections</th>          <td>   -0.6939</td> <td>    6.211</td> <td>   -0.112</td> <td> 0.911</td> <td>  -12.867</td> <td>   11.480</td>
</tr>
<tr>
  <th>Literary Criticism</th>            <td>   -7.3669</td> <td>    5.826</td> <td>   -1.264</td> <td> 0.206</td> <td>  -18.786</td> <td>    4.053</td>
</tr>
<tr>
  <th>Mathematics</th>                   <td>  -18.6358</td> <td>    5.952</td> <td>   -3.131</td> <td> 0.002</td> <td>  -30.302</td> <td>   -6.970</td>
</tr>
<tr>
  <th>Medical</th>                       <td>   -8.1662</td> <td>    5.831</td> <td>   -1.400</td> <td> 0.161</td> <td>  -19.596</td> <td>    3.263</td>
</tr>
<tr>
  <th>Music</th>                         <td>   -9.2514</td> <td>    5.829</td> <td>   -1.587</td> <td> 0.113</td> <td>  -20.677</td> <td>    2.174</td>
</tr>
<tr>
  <th>Nature</th>                        <td>    0.5946</td> <td>    5.962</td> <td>    0.100</td> <td> 0.921</td> <td>  -11.090</td> <td>   12.279</td>
</tr>
<tr>
  <th>Performing Arts</th>               <td>  -11.6704</td> <td>    5.927</td> <td>   -1.969</td> <td> 0.049</td> <td>  -23.286</td> <td>   -0.054</td>
</tr>
<tr>
  <th>Pets</th>                          <td>  -12.8346</td> <td>    6.192</td> <td>   -2.073</td> <td> 0.038</td> <td>  -24.971</td> <td>   -0.698</td>
</tr>
<tr>
  <th>Philosophy</th>                    <td>   -8.1108</td> <td>    5.850</td> <td>   -1.386</td> <td> 0.166</td> <td>  -19.577</td> <td>    3.355</td>
</tr>
<tr>
  <th>Photography</th>                   <td>   -8.0436</td> <td>    6.108</td> <td>   -1.317</td> <td> 0.188</td> <td>  -20.015</td> <td>    3.927</td>
</tr>
<tr>
  <th>Poetry</th>                        <td>    4.9192</td> <td>    5.894</td> <td>    0.835</td> <td> 0.404</td> <td>   -6.632</td> <td>   16.470</td>
</tr>
<tr>
  <th>Political Science</th>             <td>  -21.8388</td> <td>    5.842</td> <td>   -3.738</td> <td> 0.000</td> <td>  -33.288</td> <td>  -10.389</td>
</tr>
<tr>
  <th>Psychology</th>                    <td>   -6.6303</td> <td>    5.845</td> <td>   -1.134</td> <td> 0.257</td> <td>  -18.087</td> <td>    4.827</td>
</tr>
<tr>
  <th>Railroads</th>                     <td>    0.2411</td> <td>    9.075</td> <td>    0.027</td> <td> 0.979</td> <td>  -17.546</td> <td>   18.029</td>
</tr>
<tr>
  <th>Reference</th>                     <td>  -16.0700</td> <td>    5.932</td> <td>   -2.709</td> <td> 0.007</td> <td>  -27.697</td> <td>   -4.443</td>
</tr>
<tr>
  <th>Religion</th>                      <td>    0.4696</td> <td>    5.704</td> <td>    0.082</td> <td> 0.934</td> <td>  -10.710</td> <td>   11.649</td>
</tr>
<tr>
  <th>Science</th>                       <td>  -14.0122</td> <td>    5.798</td> <td>   -2.417</td> <td> 0.016</td> <td>  -25.376</td> <td>   -2.649</td>
</tr>
<tr>
  <th>Science fiction</th>               <td>  -15.6863</td> <td>    7.891</td> <td>   -1.988</td> <td> 0.047</td> <td>  -31.152</td> <td>   -0.220</td>
</tr>
<tr>
  <th>Science fiction, American</th>     <td>  -10.6350</td> <td>    8.939</td> <td>   -1.190</td> <td> 0.234</td> <td>  -28.156</td> <td>    6.886</td>
</tr>
<tr>
  <th>Self-Help</th>                     <td>    3.9991</td> <td>    5.891</td> <td>    0.679</td> <td> 0.497</td> <td>   -7.547</td> <td>   15.545</td>
</tr>
<tr>
  <th>Social Science</th>                <td>  -15.3846</td> <td>    5.757</td> <td>   -2.672</td> <td> 0.008</td> <td>  -26.668</td> <td>   -4.101</td>
</tr>
<tr>
  <th>Sports & Recreation</th>           <td>   -8.1915</td> <td>    5.818</td> <td>   -1.408</td> <td> 0.159</td> <td>  -19.595</td> <td>    3.212</td>
</tr>
<tr>
  <th>Study Aids</th>                    <td>  -53.5789</td> <td>    6.357</td> <td>   -8.429</td> <td> 0.000</td> <td>  -66.038</td> <td>  -41.120</td>
</tr>
<tr>
  <th>Technology & Engineering</th>      <td>  -19.2712</td> <td>    5.872</td> <td>   -3.282</td> <td> 0.001</td> <td>  -30.780</td> <td>   -7.762</td>
</tr>
<tr>
  <th>Transportation</th>                <td>  -15.5216</td> <td>    6.031</td> <td>   -2.574</td> <td> 0.010</td> <td>  -27.343</td> <td>   -3.700</td>
</tr>
<tr>
  <th>Travel</th>                        <td>  -20.0488</td> <td>    5.855</td> <td>   -3.424</td> <td> 0.001</td> <td>  -31.525</td> <td>   -8.573</td>
</tr>
<tr>
  <th>True Crime</th>                    <td>  -42.3630</td> <td>    6.531</td> <td>   -6.486</td> <td> 0.000</td> <td>  -55.164</td> <td>  -29.562</td>
</tr>
<tr>
  <th>United States</th>                 <td>  -10.6347</td> <td>    6.500</td> <td>   -1.636</td> <td> 0.102</td> <td>  -23.374</td> <td>    2.105</td>
</tr>
<tr>
  <th>World War, 1939-1945</th>          <td>   -6.1006</td> <td>    7.317</td> <td>   -0.834</td> <td> 0.404</td> <td>  -20.441</td> <td>    8.240</td>
</tr>
<tr>
  <th>Young Adult Fiction</th>           <td>  -15.4470</td> <td>    6.221</td> <td>   -2.483</td> <td> 0.013</td> <td>  -27.641</td> <td>   -3.253</td>
</tr>
<tr>
  <th>Young Adult Nonfiction</th>        <td>   13.6191</td> <td>    9.040</td> <td>    1.506</td> <td> 0.132</td> <td>   -4.100</td> <td>   31.338</td>
</tr>
</table>
<table class="simpletable">
<tr>
  <th>Omnibus:</th>       <td>62893.860</td> <th>  Durbin-Watson:     </th>  <td>   1.996</td> 
</tr>
<tr>
  <th>Prob(Omnibus):</th>  <td> 0.000</td>   <th>  Jarque-Bera (JB):  </th> <td>570375.112</td>
</tr>
<tr>
  <th>Skew:</th>           <td>-1.965</td>   <th>  Prob(JB):          </th>  <td>    0.00</td> 
</tr>
<tr>
  <th>Kurtosis:</th>       <td>12.123</td>   <th>  Cond. No.          </th>  <td>    347.</td> 
</tr>
</table><br/><br/>Notes:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.




```python
# Calculate frequencies
frequency = data['publisher'].value_counts()

# Define a threshold for rare categories
threshold = 10

# Group rare categories into 'Other'
data['Publisher'] = data['publisher'].apply(lambda x: x if frequency[x] > threshold else 'Other')

# Recalculate frequencies after grouping
frequency = data['Publisher'].value_counts()

# Map frequencies to the DataFrame
data['Publisher_freq'] = data['Publisher'].map(frequency)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data['Publisher_freq'] = scaler.fit_transform(data[['Publisher_freq']])
```


```python
import statsmodels.api as sm
X = data['Publisher_freq']
print(X.head())
y = data['Impact']

# Add constant term for the intercept
X = sm.add_constant(X)

# Fit the model
model = sm.OLS(y, X).fit()
```

    0   -0.167740
    1   -0.385182
    2   -0.404812
    3   -0.420001
    4   -0.244037
    Name: Publisher_freq, dtype: float64



```python
model.summary()
```




<table class="simpletable">
<caption>OLS Regression Results</caption>
<tr>
  <th>Dep. Variable:</th>         <td>Impact</td>      <th>  R-squared:         </th>  <td>   0.001</td>  
</tr>
<tr>
  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th>  <td>   0.001</td>  
</tr>
<tr>
  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th>  <td>   160.1</td>  
</tr>
<tr>
  <th>Date:</th>             <td>Sat, 10 Aug 2024</td> <th>  Prob (F-statistic):</th>  <td>1.10e-36</td>  
</tr>
<tr>
  <th>Time:</th>                 <td>16:12:39</td>     <th>  Log-Likelihood:    </th> <td>-7.7292e+05</td>
</tr>
<tr>
  <th>No. Observations:</th>      <td>138724</td>      <th>  AIC:               </th>  <td>1.546e+06</td> 
</tr>
<tr>
  <th>Df Residuals:</th>          <td>138722</td>      <th>  BIC:               </th>  <td>1.546e+06</td> 
</tr>
<tr>
  <th>Df Model:</th>              <td>     1</td>      <th>                     </th>      <td> </td>     
</tr>
<tr>
  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>      <td> </td>     
</tr>
</table>
<table class="simpletable">
<tr>
         <td></td>           <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>const</th>          <td>  786.7637</td> <td>    0.171</td> <td> 4607.194</td> <td> 0.000</td> <td>  786.429</td> <td>  787.098</td>
</tr>
<tr>
  <th>Publisher_freq</th> <td>    2.1611</td> <td>    0.171</td> <td>   12.655</td> <td> 0.000</td> <td>    1.826</td> <td>    2.496</td>
</tr>
</table>
<table class="simpletable">
<tr>
  <th>Omnibus:</th>       <td>63977.017</td> <th>  Durbin-Watson:     </th>  <td>   1.997</td> 
</tr>
<tr>
  <th>Prob(Omnibus):</th>  <td> 0.000</td>   <th>  Jarque-Bera (JB):  </th> <td>583344.742</td>
</tr>
<tr>
  <th>Skew:</th>           <td>-2.006</td>   <th>  Prob(JB):          </th>  <td>    0.00</td> 
</tr>
<tr>
  <th>Kurtosis:</th>       <td>12.210</td>   <th>  Cond. No.          </th>  <td>    1.00</td> 
</tr>
</table><br/><br/>Notes:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.




```python

```

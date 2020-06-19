# 迴圈賽程

          
## 題目
```
<ol>
    <li>設有n=2^k個運動員，要進行網球迴圈賽</li>
    <li>每個選手必須與其他n-1個選手各賽一次</li>
    <li>每個選手一天只能賽一次</li>
    <li>循環賽一共進行n-1天</li>
</ol>
```



## 分析
1.將所有的選手分為兩半，n個選手的比賽日程表可以通過為n/2個選手設計的比賽日程表來決定<br>
2、遞歸地用對選手進行分割，直到只剩下2個選手時，只要讓這2個選手進行比賽就可<br>

圖片取自於geeksforgeeks
<img src = "https://media.geeksforgeeks.org/wp-content/cdn-uploads/longest_common_prefix6.jpg"></img>



## Code

```python

```
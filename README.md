# journal_club_person_choser
Program to select a person to present (randomly and with weightings)


```python
run_jc(display=True):
```

### Example 
```python
# Journal Club Attendees
# 0 = presented last week
# 1 = default weighting
# 2 = no show last week
# 2*n = multiplier for n number of weeks no show
people = dict(Bob=1,
              Richard=0,
              Judy=1,
              Alice=1,
              Fred=4,
              John=1,
              Mike=2)
run_jc()
```
        

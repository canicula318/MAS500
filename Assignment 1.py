# count total votes counts for each personimport pandas as pddata = pd.read_csv('C:\Users\Yan_Liu\Desktop\MAS500\part one\US_election_state.csv')df = pd.DataFrame(data)Obama_total = df['Obama vote'].sum()Romney_total = df['Romney vote'].sum()print ('Obama',Obama_total,'Romney',Romney_total)
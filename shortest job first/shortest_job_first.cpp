#include<bits/stdc++.h>
using namespace std;
int main()
{
  int n,i,j,k;
  float total_wt=0.0,total_tat=0.0,ave_wt,ave_tat;
  cout<<"no of process:";
  cin>>n;
  int bt[n],wt[n],tat[n];
  cout<<"give burst time for each process:";
  for (j=0; j<n; j++)
  {
      cin>>bt[j];
  }
  sort(bt,bt+n);
  wt[0]=0;
  for (k=1;k<n;k++)
  {
      wt[k]=bt[k-1]+wt[k-1];
      total_wt=total_wt+wt[k];
  }
  for(i=0;i<n;i++)
  {
      tat[i]=bt[i]+wt[i];
      total_tat=total_tat+tat[i];
  }
ave_wt=total_wt/n;
ave_tat=total_tat/n;
cout<<"average waiting time: "<<ave_wt<<"\n";
cout<<"average waiting time: "<<ave_tat;
}

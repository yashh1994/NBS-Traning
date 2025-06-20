#include <iostream>
#include <unordered_map>
#include <bitset>


int main() { 
  void factor_ctn(int nm);
  void ctn_set_negtive(int nm,int bit);
  
  // factor_ctn(10);
  // ctn_set_negtive(-5, 4);

  x
}


void ctn_set_negtive(int nm,const int bit){
  nm = -nm;
  int max_val = 1<<bit;
  std::bitset<4> bin(max_val - nm);
  std::cout << "Negative bin for " << -nm << " is "<< bin << std::endl;
  int ctn = 0;
  for(int i = 0; i < bit; i++){
    ctn += bin[i];
  }
  std::cout << "Negative set bit count for " << -nm << " is "<< ctn << std::endl;
}



void factor_ctn(int nm){
  int temp = nm;
  int i = 2;
  std::unordered_map<int,int> mp;
  while (i <= temp){
    if(temp%i){
      i++;
    }else{
      mp[i] += 1;
      temp = temp/i;
    }
  }  
  for(auto &a: mp){
    std::cout << "Factor: "<< a.first << " * " << a.second << std::endl; 
  }
}
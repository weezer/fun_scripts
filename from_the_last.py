class Solution {
  public:
    int kEmptySlots(vector<int>& flowers, int k) {
      int n = flowers.size();
      if( n <= 1 || k >= n-1 ) return -1;
      vi space(n,0), left(n,-1), right(n,n);
      forall(i,1,n){ left[i] = i-1; }
      forall(i,0,n-1){ right[i] = i+1; }
      for( int i = n; i > 0; --i ){
        int pos = flowers[i-1] -1;
        if( pos > 0 && pos < n-1 ){
          space[pos] = 1 + space[pos-1] + space[pos+1];
          if( space[pos-1] != 0 ){
            left[pos] = left[pos-1];
            space[left[pos]+1] = space[pos];
          }
          if( space[pos+1] != 0 ){
            right[pos] = right[pos+1];
            space[right[pos]-1] = space[pos];
          }
          if( space[pos] == k && left[pos] != -1 && right[pos] != n ){
            return i-1;
          }
        }else if( pos == 0 ){
          space[pos] = 1 + space[pos+1];
          right[pos] = right[pos+1];
          space[right[pos]-1] = space[pos];
        }else if( pos == n-1 ){
          space[pos] = 1 + space[pos-1];
          left[pos] = left[pos-1];
          space[left[pos]+1] = space[pos];
        }
      }
      return -1;
    }
};
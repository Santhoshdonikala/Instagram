class GCD {
  public static void main(String[] args) {

    int n1 = 81, n2 = -153;

    // Always set to positive
    n1 = ( n1 > 0) ? n1 : -n1;
    n2 = ( n2 > 0) ? n2 : -n2;

    while(n1 != n2) {
        
      if(n1 > n2) {
        n1 -= n2;
      }
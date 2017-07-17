// includes



bool jw_search ( int *list, int size, int key, int*& rec )
{
  // Basic sequential search
  bool found = false;
  int i;

  for ( i = 0; i < size; i++ ) {
    if ( key == list[i] )
      break;
  }
  if ( i < size ) {
    found = true;
    rec = &list[i];
  }

  return found;
}



struct node {
  int rec;
  int key;
  node *next;

  node ( int r, int k, node *n )
    : rec ( r )
    , key ( k )
    , next ( n )
  {}
};



bool jw_search ( node*& list, int key, int*& rec )
{
  // Basic sequential search
  bool found = false;
  node *i;

  for ( i = list; i != 0; i = i->next ) {
    if ( key == i->key )
      break;
  }
  if ( i != 0 ) {
    found = true;
    rec = &i->rec;
  }

  return found;
}


bool jw_search ( int *list, int size, int key, int*& rec )
{
  // Quick sequential search
  bool found = false;
  int i;

  list[size] = key;
  for ( i = 0; key != list[i]; i++ )
    ;
  if ( i < size ) {
    found = true;
    rec = &list[i];
  }

  return found;
}


bool jw_search ( int *list, int size, int key, int*& rec )
{
  // Ordered sequential search
  bool found = false;
  int i;

  for ( i = 0; i < size && key > list[i]; i++ )
    ;
  if ( key == list[i] ) {
    found = true;
    rec = &list[i];
  }

  return found;
}



bool jw_search ( int *list, int size, int key, int*& rec )
{
  // Self-organizing (move to front) search
  bool found = false;

  // Is it already at the front?
  if ( key == list[0] ) {
    rec = &list[0];
    found = true;
  }
  else {
    int i;
    for ( i = 1; i < size; i++ ) {
      if ( key == list[i] )
        break;
    }
    if ( i < size ) {
      int save = list[i];
      // Fill the hole left by list[i]
      for ( int j = i; j < size - 1; j++ )
        list[j] = list[j + 1];
      // Make room at the front
      for ( int j = size - 1; j > 0; j-- )
        list[j] = list[j - 1];
      list[0] = save;
      rec = &list[0];
      found = true;
    }
  }

  return found;
}


bool jw_search ( node*& list, int key, int*& rec )
{
  // Self-organizing (move to front) search
  node *iter = list;
  bool found = false;

  // Is it already at the front?
  if ( key == iter->key ) {
    rec = &iter->rec;
    found = true;
  }
  else {
    for ( ; iter->next != 0; iter = iter->next ) {
      if ( key == iter->next->key )
        break;
    }
    // Was the item found?
    if ( iter->next != 0 ) {
      // Remove the node and fix the list
      node *save = iter->next;
      iter->next = save->next;
      // Place the node at the front
      save->next = list;
      list = save;
      rec = &list->rec;
      found = true;
    }
  }

  return found;
}



bool jw_search ( int *list, int size, int key, int*& rec )
{
  // Self-organizing (swap with previous) search
  bool found = false;
  int i;

  for ( i = 0; i < size; i++ ) {
    if ( key == list[i] )
      break;
  }
  // Was it found?
  if ( i < size ) {
    // Is it already the first?
    if ( i > 0 ) {
      int save = list[i - 1];
      list[i - 1] = list[i];
      list[i--] = save;
    }
    found = true;
    rec = &list[i];
  }

  return found;
}


bool jw_search ( int *list, int size, int key, int*& rec )
{
  // Binary search
  bool found = false;
  int low = 0, high = size - 1;

  while ( high >= low ) {
    int mid = ( low + high ) / 2;
    if ( key < list[mid] )
      high = mid - 1;
    else if ( key > list[mid] )
      low = mid + 1;
    else {
      found = true;
      rec = &list[mid];
      break;
    }
  }

  return found;
}


bool jw_search ( int *list, int size, int key, int*& rec )
{
  // Interpolation search
  bool found = false;
  int low = 0, high = size - 1;

  while ( list[high] >= key && key > list[low] ) {
    double low_diff = (double)key - list[low];
    double range_diff = (double)list[high] - list[low];
    double count_diff = (double)high - low;
    int range = (int)( low_diff / range_diff * count_diff + low );
    if ( key > list[range] )
      low = range + 1;
    else if ( key < list[range] )
      high = range - 1;
    else
      low = range;
  }
  if ( key == list[low] ) {
    found = true;
    rec = &list[low];
  }

  return found;
}




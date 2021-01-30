

var truevar = 1;
fakevar = 2;
this.fakevar2 = 3;
delete truevar  // false，删除失败
delete fakevar  // true，删除成功
delete this.fakevar2 // true，删除成功
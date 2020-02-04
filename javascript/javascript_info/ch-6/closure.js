function f()
{
  let value = 123;

  return function() {
    console.log(value);
  }
}

let g = f();

g();

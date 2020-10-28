var zero=document.getElementById('zero')
function push(obj)
{
    var pushed = obj.innerHTML
    if (pushed =='=')
    {
        zero.innerHTML=eval(zero.innerHTML);
    }
    else if (pushed == 'AC')
    {
        zero.innerHTML = '0';
    }
    else
    {
        if(zero.innerHTML=='0')
        {
            zero.innerHTML=pushed;
        }
        else
        {
            zero.innerHTML += pushed;
        }
    }
}
% rebase('base.tpl', title='Page Title')

<form action='/vnesi/' method = "POST">
<p>Vnesi temperaturo:</p>
<input type = "text" value="{{nova_temp}}" name = 'nova_temp'/>
<br/>

<p>Vnesi kraj:</p>
<input type = "text" value="{{kraj}}" name = 'kraj'/>
<br/>
<p>Vnesi dan:</p>
<input type = "text" value="{{dan}}" name = 'dan'/>
<br/>
<p>Vnesi mesec:</p>
<input type = "text" value="{{mesec}}" name = 'mesec'/>
<br/>
<p>Vnesi leto:</p>
<input type = "text" value="{{leto}}" name = 'leto'/>

<button type = 'submit'> VNESI </button>
%if napaka:
napačen vnos!
%end
</form>
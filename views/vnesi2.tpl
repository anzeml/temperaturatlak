% rebase('base.tpl', title='Page Title')

<form action='/vnesi2/' method = "POST">
<p>Vnesi tlak:</p>
<input type = "text" value="{{nov_tlak}}" name = 'nov_tlak'/>
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
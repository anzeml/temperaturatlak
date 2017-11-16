% rebase('base.tpl', title='Page Title')

<table>
<tr>
	<th><b>KRAJ</b></th>
	<th><b>TEMPERATURA</b></th>
	<th><b>TLAK</b></th>
	<th><b>GOST</b></th>
</tr>
%for kraj in podatki:
<tr>
	<td>{{kraj[0]}}</td>
	<td>{{kraj[1]}}</td>
	<td>{{kraj[2]}}</td>
	<td>{{kraj[3]}}</td>
</tr>	
%end
	
</table>
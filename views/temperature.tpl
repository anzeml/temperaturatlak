% rebase('base.tpl', title='Page Title')

<table>
<tr>
	<th><b>ID</b></th>
	<th><b>KRAJ</b></th>
	<th><b>TEMPERATURA</b></th>
	<th><b>LETO</b></th>
	<th><b>MESEC</b></th>
	<th><b>DAN</b></th>
</tr>
%for tem in podatki:
<tr>
%   for el in tem:
		<td>{{el}}</td>
%	end
%end
</tr>		
</table>
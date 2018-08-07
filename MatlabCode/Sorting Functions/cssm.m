function    out = cssm( filespec )
%   out = cssm( 'cssm.csv' )
%%    
    fid = fopen( filespec );
    cac = textscan( fid, '%*q%*q%*q%q', 'Delimiter', ',' );
    fclose( fid );
%%  
    buf = regexprep( cac{1}, '\] *\,', '];' );  % replace "]," by  "];"
    out = cell( size( buf ) );
    for jj = 1 : length( buf )
        str = buf{jj};
        out{jj} = str2num( str );
    end
end

var table = $('#table1').DataTable({
        fixedColumns: {
          left: 1
      },
      pageLength : 10,
      lengthMenu: [[10, 20, 50], [10, 20, 50]],
      "bPaginate": true, //
	  	//"searching": false, //
	  	"info":	true, //
	     "fixedHeader": true, //
       "bFilter": true,
       "bProcessing": true,


       buttons: [
             {
                     extend: 'print',
                     text: 'Print all',
                       exportOptions: {
                           modifier: {
                             selected: null
                       }
                   }
               },
           {
               extend: 'print',
               text: 'Print selected'
           }
       ],
       select: true,

       "dom": 'Brtlip'
});




var table2 = $('#table2').DataTable({
        fixedColumns: {
          left: 1
      },
      pageLength : 10,
      lengthMenu: [[10, 20, 50], [10, 20, 50]],
      "bPaginate": true, //
      "bAutoWidth": false,

	  	//"searching": false, //
	  	"info":	true, //
	     "fixedHeader": true, //
       "bFilter": true,
       "bProcessing": true,


       buttons: [
             {
                     extend: 'print',
                     text: 'Print all',
                       exportOptions: {
                           modifier: {
                             selected: null
                       }
                   }
               },
           {
               extend: 'print',
               text: 'Print selected'
           }
       ],
       select: true,

       "dom": 'Brtlip'
});

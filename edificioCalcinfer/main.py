import sqlite3
from functools import partial
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.ttk import Style


def Add_Record(top):
    main_frame = Frame(top)
    main_frame.place(x=0)
    main_frame.place(y=0)
    main_frame.place(width=740)
    main_frame.place(relheight=1)

    identification_id = Label(main_frame)
    identification_id['text'] = 'Código identificação'
    identification_id['font'] = 'Arial, 15'
    identification_id.place(x=220, y=30)
    identification_id_entry = Entry(main_frame)
    identification_id_entry.place(x=220, y=60, width=300)

    receiving_date = Label(main_frame)
    receiving_date['text'] = 'Data recebimento'
    receiving_date['font'] = 'Arial, 15'
    receiving_date.place(x=220, y=100)
    receiving_date_entry = Entry(main_frame)
    receiving_date_entry.place(x=220, y=130, width=300)

    receiving_time = Label(main_frame)
    receiving_time['text'] = 'Hora recebimento'
    receiving_time['font'] = 'Arial, 15'
    receiving_time.place(x=220, y=170)
    receiving_time_entry = Entry(main_frame)
    receiving_time_entry.place(x=220, y=200, width=300)

    identification_id_conciege = Label(main_frame)
    identification_id_conciege['text'] = 'Código porteiro'
    identification_id_conciege['font'] = 'Arial, 15'
    identification_id_conciege.place(x=220, y=240)
    identification_id_conciege_entry = Entry(main_frame)
    identification_id_conciege_entry.place(x=220, y=270, width=300)

    identification_id_apartment = Label(main_frame)
    identification_id_apartment['text'] = 'Número apartamento'
    identification_id_apartment['font'] = 'Arial, 15'
    identification_id_apartment.place(x=220, y=310)
    identification_id_apartment_entry = Entry(main_frame)
    identification_id_apartment_entry.place(x=220, y=340, width=300)

    button_submit = Button(main_frame)
    button_submit['text'] = 'Adicionar'
    button_submit['font'] = 'Arial, 15'
    button_submit['bg'] = '#f5edbf'
    button_submit['command'] = lambda: Submit(
        identification_id_entry,
        receiving_date_entry,
        receiving_time_entry,
        identification_id_conciege_entry,
        identification_id_apartment_entry
    )
    button_submit['cursor'] = 'hand2'
    button_submit['border'] = '2'
    button_submit.place(x=310, y=389, width=100)


def Display_Records(win, top):
    main_frame = Frame(top)
    main_frame.place(x=0)
    main_frame.place(y=0)
    main_frame.place(width=740)
    main_frame.place(relheight=1)

    # Defining two scrollbars
    scroll_x = ttk.Scrollbar(main_frame, orient=HORIZONTAL)
    scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)

    columns = ('id_encomenda', 'data_recebimento', 'hora_recebimento', 'id_colaborador', 'numero_apartamento')

    style = Style()
    style.configure('Treeview', background='#d8bff5', font='Arial 12', )

    treeview = ttk.Treeview(main_frame)
    treeview['columns'] = columns
    treeview['height'] = 400
    treeview['selectmode'] = 'extended'
    treeview['yscrollcommand'] = scroll_y.set
    treeview['xscrollcommand'] = scroll_x.set

    scroll_y.config(command=treeview.yview)
    scroll_y.pack(side=LEFT, fill=Y)
    scroll_x.config(command=treeview.xview)
    scroll_x.pack(side=BOTTOM, fill=X)

    # Table headings
    treeview.heading('id_encomenda', text='Código identificação', anchor=W)
    treeview.heading('data_recebimento', text='Data Recebimento', anchor=W)
    treeview.heading('hora_recebimento', text='Hora recebimento', anchor=W)
    treeview.heading('id_colaborador', text='Codigo porteiro', anchor=W)
    treeview.heading('numero_apartamento', text='Número apartamento', anchor=W)
    treeview.pack()

    try:
        connection = sqlite3.connect('calcinfer_database.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Encomenda')
        rows = cursor.fetchall()

        if rows is None:
            messagebox.showerror(
                'Banco de Dados Vazio',
                'Nenhum dado para ser exibido!',
                parent=window
            )
            connection.close()
            Clear_Screen(win, top)
        else:
            connection.close()

    except Exception as e:
        messagebox.showerror(
            'Erro!',
            f'Error ao exibir encomenda',
            parent=window
        )
        print(e)

    for list in rows:
        treeview.insert(
            '',
            'end',
            text=(rows.index(list) + 1),
            values=(list[0], list[1], list[2], list[3], list[4])
        )


def Show_Records(top, rows):
    main_frame = Frame(top)
    main_frame.place(x=0)
    main_frame.place(y=0)
    main_frame.place(width=740)
    main_frame.place(relheight=1)

    # Defining two scrollbars
    scroll_x = ttk.Scrollbar(main_frame, orient=HORIZONTAL)
    scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)

    columns = ('id_encomenda', 'data_recebimento', 'hora_recebimento', 'id_colaborador', 'numero_apartamento')

    treeview = ttk.Treeview(main_frame)
    treeview['columns'] = columns
    treeview['height'] = 400
    treeview['selectmode'] = 'extended'
    treeview['yscrollcommand'] = scroll_y.set
    treeview['xscrollcommand'] = scroll_x.set

    scroll_y.config(command=treeview.yview)
    scroll_y.pack(side=LEFT, fill=Y)
    scroll_x.config(command=treeview.xview)
    scroll_x.pack(side=BOTTOM, fill=X)

    # Table headings
    treeview.heading('id_encomenda', text='Código identificação', anchor=W)
    treeview.heading('data_recebimento', text='Data Recebimento', anchor=W)
    treeview.heading('hora_recebimento', text='Hora recebimento', anchor=W)
    treeview.heading('id_colaborador', text='Codigo porteiro', anchor=W)
    treeview.heading('numero_apartamento', text='Número apartamento', anchor=W)
    treeview.pack()
    treeview.bind('<Double-Button-1>')

    for list in rows:
        treeview.insert(
            '',
            'end',
            text=(rows.index(list) + 1),
            values=(list[0], list[1], list[2], list[3], list[4])
        )


def Check_Order_To_Search(top, order_id_entry):
    if order_id_entry.get() == '':
        messagebox.showerror(
            'Erro',
            'Favor informar um código!',
            parent=window
        )
    else:
        try:
            connection = sqlite3.connect('calcinfer_database.db')
            cursor = connection.cursor()

            cursor.execute('SELECT * FROM Encomenda WHERE id_encomenda = ?', [order_id_entry.get()])
            rows = cursor.fetchall()

            if len(rows) == 0:
                messagebox.showerror(
                    'Erro!',
                    f'O código {order_id_entry.get()}, não existe ou não está cadastrado!',
                    parent=window
                )
                connection.close()
            else:
                Show_Records(top, rows)
                connection.close()

            order_id_entry.delete(0, END)

        except Exception as e:
            messagebox.showerror(
                'Erro!',
                f'Error ao buscar encomenda',
                parent=window
            )
            print(e)

        finally:
            order_id_entry.delete(0, END)


def Get_Order_To_Search(top):
    main_frame = Frame(top)
    main_frame.place(x=0)
    main_frame.place(y=0)
    main_frame.place(width=740)
    main_frame.place(relheight=1)

    order_id = Label(main_frame)
    order_id['text'] = 'BUSCAR - Informe o código da encomenda!'
    order_id['font'] = 'Arial, 15'
    order_id.place(x=135, y=60, width=510)
    order_id_entry = Entry(main_frame)
    order_id_entry.place(x=200, y=100, width=200)

    submit_button = Button(main_frame)
    submit_button['text'] = 'Buscar'
    submit_button['font'] = 'Arial, 12'
    submit_button['bg'] = '#bfddf5'
    submit_button['bd'] = 2
    submit_button['command'] = lambda: Check_Order_To_Search(top, order_id_entry)
    submit_button['cursor'] = 'hand2'
    submit_button.place(x=200, y=150, width=100)


def Update_Record(row, id_entry, date_entry, time_entry, conciege_entry, apartment_entry):
    if (
            id_entry.get() == '' or
            date_entry.get() == '' or
            time_entry.get() == '' or
            conciege_entry.get() == '' or
            apartment_entry.get() == ''
    ):
        messagebox.showerror(
            "Error!",
            "Preenha todos os campos",
            parent=window
        )
    else:
        try:
            connection = sqlite3.connect('calcinfer_database.db')
            cursor = connection.cursor()

            cursor.execute(
                'SELECT * FROM Encomenda WHERE id_encomenda = ?',
                [row[0]]
            )

            row = cursor.fetchone()

            if row is None:
                messagebox.showerror(
                    'Erro',
                    f'O código: {id_entry.get()} não existe, favor informar um código válido!',
                    parent=window
                )
            else:
                cursor.execute(
                    'UPDATE Encomenda SET data_recebimento = ?, hora_recebimento = ?, id_colaborador = ?, numero_apartamento = ? WHERE id_encomenda = ?',
                    (
                        date_entry.get(),
                        time_entry.get(),
                        conciege_entry.get(),
                        apartment_entry.get(),
                        row[0]
                    )
                )

                connection.commit()
                connection.close()

                messagebox.showinfo(
                    'Sucesso!',
                    'Encomenda atualizada com Sucesso!'
                )

                Reset_Field(
                    id_entry,
                    date_entry,
                    time_entry,
                    conciege_entry,
                    apartment_entry
                )

        except Exception as e:
            messagebox.showerror(
                'Erro!',
                f'Error ao atualizar encomenda',
                parent=window
            )
            print(e)


def Get_data_To_Update(top, row):
    main_frame = Frame(top)
    main_frame.place(x=0)
    main_frame.place(y=0)
    main_frame.place(width=740)
    main_frame.place(relheight=1)

    identification_id = Label(main_frame)
    identification_id['text'] = 'Código identificação'
    identification_id['font'] = 'Arial, 15'
    identification_id.place(x=220, y=30)
    identification_id_entry = Entry(main_frame)
    identification_id_entry.insert(0, row[0])
    identification_id_entry.place(x=220, y=60, width=300)

    receiving_date = Label(main_frame)
    receiving_date['text'] = 'Data recebimento'
    receiving_date['font'] = 'Arial, 15'
    receiving_date.place(x=220, y=100)
    receiving_date_entry = Entry(main_frame)
    receiving_date_entry.insert(0, row[1])
    receiving_date_entry.place(x=220, y=130, width=300)

    receiving_time = Label(main_frame)
    receiving_time['text'] = 'Hora recebimento'
    receiving_time['font'] = 'Arial, 15'
    receiving_time.place(x=220, y=170)
    receiving_time_entry = Entry(main_frame)
    receiving_time_entry.insert(0, row[2])
    receiving_time_entry.place(x=220, y=200, width=300)

    identification_id_conciege = Label(main_frame)
    identification_id_conciege['text'] = 'Código porteiro'
    identification_id_conciege['font'] = 'Arial, 15'
    identification_id_conciege.place(x=220, y=240)
    identification_id_conciege_entry = Entry(main_frame)
    identification_id_conciege_entry.insert(0, row[3])
    identification_id_conciege_entry.place(x=220, y=270, width=300)

    identification_id_apartment = Label(main_frame)
    identification_id_apartment['text'] = 'Número apartamento'
    identification_id_apartment['font'] = 'Arial, 15'
    identification_id_apartment.place(x=220, y=310)
    identification_id_apartment_entry = Entry(main_frame)
    identification_id_apartment_entry.insert(0, row[4])
    identification_id_apartment_entry.place(x=220, y=340, width=300)

    button_update = Button(main_frame)
    button_update['text'] = 'Atualizar'
    button_update['font'] = 'Arial, 15'
    button_update['bg'] = '#c2f5bf'
    button_update['command'] = partial(
        Update_Record,
        row,
        identification_id_entry,
        receiving_date_entry,
        receiving_time_entry,
        identification_id_conciege_entry,
        identification_id_apartment_entry
    )
    button_update['cursor'] = 'hand2'
    button_update['border'] = '2'
    button_update.place(x=220, y=389, width=130)

    button_cancel = Button(main_frame)
    button_cancel['text'] = 'Cancelar'
    button_cancel['font'] = 'Arial, 15'
    button_cancel['bg'] = '#f5c4bf'
    button_cancel['command'] = lambda: Reset_Field(
        identification_id_entry,
        receiving_date_entry,
        receiving_time_entry,
        identification_id_conciege_entry,
        identification_id_apartment_entry
    )
    button_cancel['cursor'] = 'hand2'
    button_cancel['border'] = '2'
    button_cancel.place(x=390, y=389, width=130)


def Check_Order_To_Update(top, order_id_entry):
    if order_id_entry.get() == '':
        messagebox.showerror(
            'Erro',
            'Favor informar um código!',
            parent=window
        )
    else:
        try:
            connection = sqlite3.connect('calcinfer_database.db')
            cursor = connection.cursor()

            cursor.execute('SELECT * FROM Encomenda WHERE id_encomenda = ?', [order_id_entry.get()])
            row = cursor.fetchone()

            if row is None:
                messagebox.showerror(
                    'Erro',
                    f'Não existe encomenda registrada com o código: {order_id_entry.get()}, favor informar código válido',
                    parent=window
                )
                connection.close()
            else:
                Get_data_To_Update(top, row)
                connection.close()

        except Exception as e:
            messagebox.showerror(
                'Erro!',
                f'Error ao buscar encomenda',
                parent=window
            )
            print(e)

        finally:
            order_id_entry.delete(0, END)


def Check_Order_To_Delete(order_id_entry):
    if order_id_entry.get() == '':
        messagebox.showerror(
            'Erro',
            'Favor informar um código!',
            parent=window
        )
    else:
        try:
            connection = sqlite3.connect('calcinfer_database.db')
            cursor = connection.cursor()

            cursor.execute(
                'SELECT * FROM Encomenda WHERE id_encomenda = ?',
                [order_id_entry.get()]
            )

            row = cursor.fetchone()

            if row is None:
                messagebox.showerror(
                    'Erro',
                    f'O código: {order_id_entry.get()} não existe, favor informar um código válido!',
                    parent=window
                )
            else:
                var = messagebox.askokcancel(
                    'Deletar dado',
                    f'Confirmar exclusão de encomenda código {order_id_entry.get()}?',
                    parent=window
                )

                if var:
                    cursor.execute(
                        'DELETE from Encomenda WHERE id_encomenda = ?',
                        [order_id_entry.get()]
                    )

                    connection.commit()

                    messagebox.showinfo(
                        'Sucesso!',
                        'Encomenda deletada com Sucesso!'
                    )

                connection.close()

        except Exception as e:
            messagebox.showerror(
                'Erro!',
                f'Error ao atualizar encomenda',
                parent=window
            )
            print(e)

        finally:
            order_id_entry.delete(0, END)


def Update_Data(top):
    main_frame = Frame(top)
    main_frame.place(x=0)
    main_frame.place(y=0)
    main_frame.place(width=740)
    main_frame.place(relheight=1)

    order_id = Label(main_frame)
    order_id['text'] = 'ATUALIZAR - Informe o código da encomenda!'
    order_id['font'] = 'Arial, 15'
    order_id.place(x=155, y=60, width=510)
    order_id_entry = Entry(main_frame)
    order_id_entry.place(x=200, y=100, width=200)

    submit_button = Button(main_frame)
    submit_button['text'] = 'Atualizar'
    submit_button['bg'] = '#c2f5bf'
    submit_button['font'] = 'Arial, 12'
    submit_button['bd'] = 2
    submit_button['command'] = lambda: Check_Order_To_Update(top, order_id_entry)
    submit_button['cursor'] = 'hand2'
    submit_button.place(x=200, y=150, width=100)


def Delete_Data(top):
    main_frame = Frame(top)
    main_frame.place(x=0)
    main_frame.place(y=0)
    main_frame.place(width=740)
    main_frame.place(relheight=1)

    order_id = Label(main_frame)
    order_id['text'] = 'DELETAR - Informe o código da encomenda!'
    order_id['font'] = 'Arial, 15'
    order_id.place(x=145, y=60, width=510)
    order_id_entry = Entry(main_frame)
    order_id_entry.place(x=200, y=100, width=200)

    submit_button = Button(main_frame)
    submit_button['text'] = 'Deletar'
    submit_button['bg'] = '#f5c4bf'
    submit_button['font'] = 'Arial, 12'
    submit_button['bd'] = 2
    submit_button['command'] = lambda: Check_Order_To_Delete(order_id_entry)
    submit_button['cursor'] = 'hand2'
    submit_button.place(x=200, y=150, width=100)


def Clear_Screen(win, top):
    top.destroy()
    win.deiconify()


def Reset_Field(id_entry, date_entry, time_entry, conciege_entry, apartment_entry):
    id_entry.delete(0, END)
    date_entry.delete(0, END)
    time_entry.delete(0, END)
    conciege_entry.delete(0, END)
    apartment_entry.delete(0, END)


def Submit(id_entry, date_entry, time_entry, conciege_entry, apartment_entry):
    if (
            id_entry.get() == '' or
            date_entry.get() == '' or
            time_entry.get() == '' or
            conciege_entry.get() == '' or
            apartment_entry.get() == ''
    ):
        messagebox.showerror(
            "Error!",
            "Preenha todos os campos",
            parent=window
        )
    else:
        try:
            connection = sqlite3.connect('calcinfer_database.db')
            cursor = connection.cursor()

            cursor.execute(
                'SELECT * FROM Encomenda WHERE id_encomenda = ?',
                [id_entry.get()]
            )

            row = cursor.fetchone()

            if row is not None:
                messagebox.showerror(
                    'Erro',
                    f'Já existe uma encomenda registrada com o código: {id_entry.get()}, favor informar outro código',
                    parent=window
                )
            else:
                cursor.execute(
                    'INSERT INTO Encomenda(id_encomenda, data_recebimento, hora_recebimento, id_colaborador, numero_apartamento) VALUES(?, ?, ?, ?, ?)',
                    (
                        id_entry.get(),
                        date_entry.get(),
                        time_entry.get(),
                        conciege_entry.get(),
                        apartment_entry.get()
                    )
                )

                connection.commit()
                connection.close()

                messagebox.showinfo(
                    'Sucesso!',
                    'Encomenda cadastrada com Sucesso!'
                )

                Reset_Field(
                    id_entry,
                    date_entry,
                    time_entry,
                    conciege_entry,
                    apartment_entry
                )

        except Exception as e:
            messagebox.showerror(
                'Erro!',
                f'Error ao registrar encomenda',
                parent=window
            )
            print(e)


def Exit(win):
    win.destroy()


def Open_Frame_Register_Order(win):
    win.iconify()
    top = Toplevel()
    top.title('Projeto de Extensão Estácio de Sá')
    top.geometry('%dx%d+%d+%d' % (width, height, position_x, position_y))
    top.resizable(False, False)
    frame_registrar_encomenda = Frame(top)
    frame_registrar_encomenda.place(x=0)
    frame_registrar_encomenda.place(y=0)
    frame_registrar_encomenda.place(width=740)
    frame_registrar_encomenda.place(relheight=1)

    # Left Frame
    frame_1 = Frame(top)
    frame_1.place(x=0)
    frame_1.place(y=0)
    frame_1.place(width=740)
    frame_1.place(relheight=1)

    frame_2 = Frame(top)
    frame_2.place(x=740)
    frame_2.place(y=0)
    frame_2.place(relwidth=1)
    frame_2.place(relheight=1)

    mensagem_registro = "Utilize os botões laterais \npara registrar e consultar encomendas"
    msg_registro = Message(frame_1, text=mensagem_registro)
    msg_registro.config(font=('Arial', 30, 'italic'), justify="center", padx=90, pady=200)
    msg_registro.pack()

    button_add_new = Button(frame_2)
    button_add_new['text'] = 'Adicionar'
    button_add_new['font'] = 'Arial, 12'
    button_add_new['bg'] = '#f5edbf'
    button_add_new['bd'] = 2
    button_add_new['border'] = 3
    button_add_new['command'] = lambda: Add_Record(top)
    button_add_new['cursor'] = 'hand2'
    button_add_new.place(x=50, y=40, width=100)

    button_display = Button(frame_2)
    button_display['text'] = 'Exibir'
    button_display['font'] = 's.font_1, 12'
    button_display['bd'] = 2
    button_display['bg'] = '#d8bff5'
    button_display['border'] = 3
    button_display['command'] = lambda: Display_Records(win, top)
    button_display['cursor'] = 'hand2'
    button_display.place(x=50, y=100, width=100)

    button_search = Button(frame_2)
    button_search['text'] = 'Buscar'
    button_search['bg'] = '#bfddf5'
    button_search['font'] = 'Arial, 12'
    button_search['bd'] = 2
    button_search['border'] = 3
    button_search['command'] = lambda: Get_Order_To_Search(top)
    button_search['cursor'] = 'hand2'
    button_search.place(x=50, y=160, width=100)

    button_update = Button(frame_2)
    button_update['text'] = 'Atualizar'
    button_update['font'] = 'Arial, 12'
    button_update['bd'] = 2
    button_update['bg'] = '#c2f5bf'
    button_update['border'] = 3
    button_update['command'] = lambda: Update_Data(top)
    button_update['cursor'] = 'hand2'
    button_update.place(x=50, y=220, width=100)

    button_delete = Button(frame_2)
    button_delete['text'] = 'Deletar'
    button_delete['font'] = 'Arial, 12'
    button_delete['bg'] = '#f5c4bf'
    button_delete['bd'] = 2
    button_delete['border'] = 3
    button_delete['command'] = lambda: Delete_Data(top)
    button_delete['cursor'] = 'hand2'
    button_delete.place(x=50, y=280, width=100)

    button_clear = Button(frame_2)
    button_clear['text'] = 'Limpar'
    button_clear['font'] = 'Arial, 12'
    button_clear['bd'] = 2
    button_clear['border'] = 3
    button_clear['command'] = lambda: Clear_Screen(win, top)
    button_clear['cursor'] = 'hand2'
    button_clear.place(x=50, y=340, width=100)

    button_exit = Button(frame_2)
    button_exit['text'] = 'Sair'
    button_exit['font'] = 'Arial 12'
    button_exit['bd'] = 2
    button_exit['border'] = 3
    button_exit['command'] = lambda: Exit(win)
    button_exit['cursor'] = 'hand2'
    button_exit.place(x=50, y=400, width=100)


def Create_Tables_DB():
    global connection, cursor
    try:
        connection = sqlite3.connect('calcinfer_database.db')
        cursor = connection.cursor()

        sql_create_table__collaborator = ''' CREATE TABLE IF NOT EXISTS Colaborador(
               id_colaborador integer NOT NULL,
               nome text NOT NULL,
               CONSTRAINT COLABORADOR_pk PRIMARY KEY(id_colaborador)
        );'''

        sql_create_table__client = '''CREATE TABLE IF NOT EXISTS Cliente(
            numero_apartamento integer NOT NULL,
            nome text NOT NULL,
            CONSTRAINT CLIENTE_pk PRIMARY KEY (numero_apartamento)
        );'''

        sql_create_table__order = '''CREATE TABLE IF NOT EXISTS Encomenda(
            id_encomenda integer NOT NULL,
            data_recebimento text NOT NULL,
            hora_recebimento text NOT NULL,
            id_colaborador integer NOT NULL,
            numero_apartamento integer NOT NULL,
            CONSTRAINT ENCOMENDA_pk PRIMARY KEY (id_encomenda),
            CONSTRAINT ENCOMENDA_COLABORADOR FOREIGN KEY (id_colaborador) REFERENCES Colaborador (id_colaborador),
            CONSTRAINT ENCOMENDA_CLIENTE FOREIGN KEY (numero_apartamento) REFERENCES Cliente (numero_apartamento) 
        );'''

        sql_create_table__delivery_order = '''CREATE TABLE IF NOT EXISTS Entregaencomenda(
            id_entrega_encomenda integer NOT NULL,
            data_entrega text NOT NULL,
            hora_entrega text NOT NULL,
            id_encomenda integer NOT NULL,
            id_colaborador integer NOT NULL,
            numero_apartamento integer NOT NULL,
            nome_cliente text NOT NULL,
            CONSTRAINT ENTREGAENCOMENDA_pk PRIMARY KEY (id_entrega_encomenda),
            CONSTRAINT ENTREGAENCOMENDA_ENCOMENDA FOREIGN KEY (id_encomenda) REFERENCES encomenda (id_encomenda),
            CONSTRAINT ENTREGAENCOMENDA_COLABORADOR FOREIGN KEY (id_colaborador) REFERENCES colaborador (id_colaborador),
            CONSTRAINT ENTREGAENCOMENDA_CLIENTE FOREIGN KEY (numero_apartamento) REFERENCES cliente (numero_apartamento) 
        );'''

        cursor.execute(sql_create_table__collaborator)
        cursor.execute(sql_create_table__client)
        cursor.execute(sql_create_table__order)
        cursor.execute(sql_create_table__delivery_order)

        connection.commit()

        messagebox.showinfo(
            'Sucesso',
            'Tabelas criadas com sucesso!'
        )

    except sqlite3.DatabaseError as err:
        messagebox.showerror(
            'Erro',
            'Erro ao criar tabelas no Banco de Dados'
        )
        print(err)
    finally:
        if connection:
            cursor.close()
            connection.close()
            # print('-≥ Conexão com o Banco de Dados finalizada!')


def Insert_Collaborator_Into_Table():
    try:
        connection = sqlite3.connect('calcinfer_database.db')
        cursor = connection.cursor()

        sql_insert_table__collaborator_marcos = 'INSERT INTO Colaborador(id_colaborador, nome) VALUES(1, "Marcos");'
        sql_insert_table__collaborator_anderson = 'INSERT INTO Colaborador(id_colaborador, nome) VALUES(2, "Anderson");'

        cursor.execute(sql_insert_table__collaborator_marcos)
        cursor.execute(sql_insert_table__collaborator_anderson)

        connection.commit()

        messagebox.showinfo(
            'Sucesso',
            'Coladoradores inseridos com sucesso!'
        )

    except sqlite3.DatabaseError as err:
        messagebox.showerror(
            'Erro',
            'Erro ao inserir colaboradores no Banco de Dados'
        )
        print(err)
    finally:
        if connection:
            cursor.close()
            connection.close()
            # print('-≥ Conexão com o Banco de Dados finalizada!')


def Insert_Client_Into_Table():
    try:
        connection = sqlite3.connect('calcinfer_database.db')
        cursor = connection.cursor()

        sql_insert_table__client_1 = 'INSERT INTO Cliente(numero_apartamento, nome) VALUES(1, "Cliente 1");'
        sql_insert_table__client_2 = 'INSERT INTO Cliente(numero_apartamento, nome) VALUES(2, "Cliente 2");'
        sql_insert_table__client_3 = 'INSERT INTO Cliente(numero_apartamento, nome) VALUES(3, "Cliente 3");'
        sql_insert_table__client_4 = 'INSERT INTO Cliente(numero_apartamento, nome) VALUES(4, "Cliente 4");'
        sql_insert_table__client_5 = 'INSERT INTO Cliente(numero_apartamento, nome) VALUES(5, "Cliente 5");'

        cursor.execute(sql_insert_table__client_1)
        cursor.execute(sql_insert_table__client_2)
        cursor.execute(sql_insert_table__client_3)
        cursor.execute(sql_insert_table__client_4)
        cursor.execute(sql_insert_table__client_5)

        connection.commit()

        messagebox.showinfo(
            'Sucesso',
            'Clientes inseridos com sucesso!'
        )

    except sqlite3.DatabaseError as err:
        messagebox.showerror(
            'Erro',
            'Erro ao inserir clientes no Banco de Dados'
        )
        print(err)
    finally:
        if connection:
            cursor.close()
            connection.close()
            # print('-≥ Conexão com o Banco de Dados finalizada!')


'''------------------------------------------- main -------------------------------------------'''
window = Tk()
window.title('Projeto de Extensão Estácio de Sá')

# dimensoes da janela
width = 900
height = 500

# resolução do nosso sistema
width_screen = window.winfo_screenwidth()
height_screen = window.winfo_screenheight()

# posicao da janela
position_x = width_screen / 2 - width / 2
position_y = height_screen / 2 - height / 2

# definir geometry
window.geometry('%dx%d+%d+%d' % (width, height, position_x, position_y))
window.resizable(False, False)

#Create_Tables_DB()
#Insert_Collaborator_Into_Table()
#Insert_Client_Into_Table()

initial_frame = Frame(window)
initial_frame.place(x=0)
initial_frame.place(y=0)
initial_frame.place(width=900)
initial_frame.place(relheight=1)

initial_message = "Registro de encomendas\nEdifício Calcinfer"
msg = Message(initial_frame, text=initial_message)
msg.config(font=('Arial', 40, 'italic'), justify="center", padx=20, pady=70)
msg.pack()

button_register_order = Button(initial_frame)
button_register_order['command'] = lambda: Open_Frame_Register_Order(window)
button_register_order['text'] = 'INICIAR'
button_register_order['font'] = 'Arial 20'
button_register_order['bd'] = 9
button_register_order['relief'] = 'groove'
button_register_order['width'] = 10
button_register_order.pack()

window.mainloop()

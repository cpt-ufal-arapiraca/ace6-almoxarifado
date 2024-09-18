import home from '../assets/inicio.png';
import exit from '../assets/saida.png'
import notification from '../assets/notificacoes.png'
import settings from '../assets/configuracoes.png';
import report from '../assets/dashboard.png';
import orders from '../assets/pedidos.png';
import stock from '../assets/estoque.png';

const PerfilIcon = () =>{

  return(
    <div className='container-perfil'>

          <div class="icon-perfil"><img></img></div>
          <div class="name-perfil">Olá, </div>

    </div>
  )

}

const AdminNavBar = () => {
    return (
      <div className="containerLeft">

        <PerfilIcon></PerfilIcon>

        <div className='container-options'>

          <div class="options home" >

            <div class="icon-options "><img src={home}></img></div>
            <div class="text-options">Início</div>

          </div>
  
          <div class="options settings" >

            <div class="icon-options "><img src={settings}></img></div>
            <div class="text-options">Configurações</div>

          </div>    
  
          <div class="options notification" >

            <div class="icon-options "><img src={notification}></img></div>
            <div class="text-options">Notificações</div>

          </div>

          <div className="separator-line"></div>

          <div class="options orders" >

            <div class="icon-options "><img src={orders}></img></div>
            <div class="text-options">Pedidos</div>

          </div>

          <div class="options stock" >

            <div class="icon-options "><img src={stock}></img></div>
            <div class="text-options">Estoque</div>

          </div>

          <div class="options report" >

            <div class="icon-options "><img src={report}></img></div>
            <div class="text-options">Relatorio</div>

          </div>

  
          <div className="separator-line line-bottom"></div>
  
          
          <div class="options exit" >

            <div class="icon-options "><img src={exit}></img></div>
            <div class="text-options">Sair</div>

          </div>
          
  
          <div className="direitos bottom">
            Todos os direitos reservados ©
          </div>
        </div>
      </div>
    );
  };

  export default AdminNavBar;
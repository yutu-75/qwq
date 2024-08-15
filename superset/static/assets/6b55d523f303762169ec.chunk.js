"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[60665],{462505:(t,e,a)=>{a.r(e),a.d(e,{default:()=>Y});var r=a(667294),o=a(828216),n=a(211965),s=a(997183),i=a(71577),c=a(113013),d=a(115926),l=a.n(d),h=a(929119),p=a(455867),u=a(431069),m=a(827167),f=a(652924),g=a(958452),y=a(667496),v=a(591877),w=a(593185),x=a(440768),I=a(34858),S=a(232228),b=a(419259),Z=a(838703),k=a(414114),C=a(983673),T=a(727989),D=a(107447),R=a(166683),_=a(330115),F=a(454076),z=a(755961),E=a(683862),M=a(49937),N=a(14890),q=a(132657),A=a(935500),O=a(23525),P=a(427600),Q=a(748086);let j=0;class H extends r.Component{constructor(t){super(t),this.setChartData=t=>{this.setState((e=>({chartData:{...e.chartData,queriesResponse:t.charts.charts[this.props.chartId].queriesResponse}})))},this.getDeal=t=>{let e={...this.state};return this.setState({ChartOpen:!1}),u.Z.get({endpoint:`/api/v1/explore/?slice_id=${t}`}).then((a=>{const r=a.json.result;this.props.actions.getSavedChart(r.form_data,r.force||(0,O.eY)(P.KD.force),300,t,this.props.dashboardId,this.props.ownState).then((t=>{t[0].queriesResponse&&t[0].queriesResponse[0].message&&0==j&&(j=1,Q.ZP.error(t[0].queriesResponse[0].message),setTimeout((()=>{j=0}),2e3))}));const{queriesResponse:o}=this.props.charts.charts[this.props.chartId];e={width:"100%",height:window.innerHeight-120,ownState:this.props.ownState,annotationData:void 0,chartAlert:null,chartStackTrace:null,chartId:t,chartIsStale:!1,chartStatus:"success",triggerRender:!1,force:!1,datasource:r.dataset,errorMessage:null,formData:r.form_data,latestQueryFormData:r.form_data,onQuery:void 0,queriesResponse:o,setControlValue:void 0,timeout:300,triggerQuery:!1,vizType:r.form_data.viz_type,chartTitle:this.props.chartTitle},this.setState({ChartOpen:!0,chartData:e})}))},this.state={ChartOpen:!1,ownState:void 0,queriesResponse:void 0,chartId:void 0,chartTitle:"",chartData:{}}}UNSAFE_componentWillReceiveProps(t){this.props.chartId!==t.chartId&&this.getDeal(t.chartId)}componentDidMount(){this.setState({chartId:this.props.chartId,chartTitle:this.props.chartTitle}),this.getDeal(this.props.chartId)}UNSAFE_componentWillUpdate(t){this.props.charts.charts[this.props.chartId]&&t.charts.charts[this.props.chartId]!==this.props.charts.charts[this.props.chartId]&&this.setChartData(t)}render(){const{ChartOpen:t,chartData:e}=this.state;return(0,n.tZ)(M.Ak,{style:{border:"10px solid #f0f2f5",padding:"0",paddingLeft:"10px",maxHeight:"calc(100vh - 100px)",overflowY:"auto"},className:"chartCard"},t&&e&&(0,n.tZ)(q.Z,{width:e.width,height:e.height,ownState:e.ownState,annotationData:e.annotationData,chartAlert:e.chartAlert,chartStackTrace:e.chartStackTrace,chartId:e.chartId,chartStatus:e.chartStatus,triggerRender:e.triggerRender,force:e.force,datasource:e.datasource,errorMessage:e.errorMessage,formData:e.formData,latestQueryFormData:e.latestQueryFormData,onQuery:e.onQuery,queriesResponse:e.queriesResponse,chartIsStale:e.chartIsStale,setControlValue:e.setControlValue,timeout:e.timeout,triggerQuery:e.triggerQuery,vizType:e.vizType,chartTitle:this.props.chartTitle}))}}const $=(0,o.$j)((function(t){return{ownState:t.dataMask?t.dataMask.ownState:void 0}}),(function(t){const e={...A};return{actions:(0,N.DE)(e,t)}}))(H),{Sider:U,Content:V}=s.Z;let B={chartId:0,pid:0,perm:0};const L=(0,p.t)('The passwords for the databases below are needed in order to import them together with the charts. Please note that the "Secure Extra" and "Certificate" sections of the database configuration are not present in export files, and should be added manually after the import if they are needed.'),W=(0,p.t)("You are importing one or more charts that already exist. Overwriting might cause you to lose some of your work. Are you sure you want to overwrite?");(0,D.Z)();const Y=(0,k.ZP)((function(t){const{addDangerToast:e,addSuccessToast:a}=t,{state:{resourceCollection:s},setResourceCollection:d,hasPerm:k,refreshData:D}=(0,I.Yi)("chart",(0,p.t)("chart"),e),[M,N]=(0,r.useState)("240"),[q,A]=(0,r.useState)("240"),[O,P]=(0,r.useState)(!1),[Q,j]=(0,r.useState)(0),H=(0,o.v9)((t=>t.charts)),Y={Import:(0,p.t)("Import"),newbuilt:(0,p.t)("New Chart"),adddev_menu:(0,p.t)("Edit Chart"),adddev_name:(0,p.t)("Chart Name"),width:M},{sliceCurrentlyEditing:G,handleChartUpdated:K,closeChartEditModal:X}=(0,I.fF)(d,s),[J,tt]=(0,r.useState)(!1),[et,at]=(0,r.useState)([]),[rt,ot]=(0,r.useState)(!1),[nt,st]=(0,r.useState)(!1),[it,ct]=(0,r.useState)(""),[dt,lt]=(0,r.useState)("");(0,r.useEffect)((()=>{sessionStorage.removeItem("dashboardGroup_id")}),[]),(0,r.useEffect)((()=>{B.chartId&&u.Z.get({endpoint:`/api/v1/explore/?slice_id=${B.chartId}`}).then((async t=>{const e=t.json.result;lt(e)}))}),[B.chartId]),k("can_write");const ht=k("can_write"),pt=k("can_export")&&(0,v.cr)(w.T.VERSIONED_EXPORT),ut=t=>{const e=t.map((({id:t})=>t));(0,S.Z)("chart",e,(()=>{ot(!1)})),ot(!0)};(0,r.useEffect)((()=>{let t=sessionStorage.getItem("chartIds"),e=sessionStorage.getItem("chartTitle");return t&&(B.chartId=t,ct(e)),()=>{-1!=window.location.pathname.indexOf("/chart/list/")&&-1!=window.location.pathname.indexOf("/explore/")||(sessionStorage.removeItem("chartIds"),sessionStorage.removeItem("chartTitle"),B.chartId=0)}}),[window.location.pathname]);const mt=()=>{P(!O),N(O?240:"0"),A(O?240:"0")},ft=(0,F.w)(),gt=(0,r.useMemo)((()=>{var t;return B.chartId&&(null==(t=H[B.chartId])?void 0:t.changedInfo)||{}}),[B.chartId,H]);return(0,n.tZ)(E.Rh,null,ft&&(0,n.tZ)(n.xB,{styles:n.iv`
            // 头部
            .ant-layout-sider-children .ant-card-body {
              padding: 10px;
              border: 0;
              color: #000 !important;
            }
            // 整体背景
            .ant-layout-sider-children,
            .ant-menu.ant-menu-dark,
            .ant-input-search,
            .ant-layout-sider-children .ant-card,
            .ant-layout-sider-children .ant-layout {
              background: #ffffff !important;
            }
            // 搜索框
            .inputcss .ant-input-affix-wrapper {
              background-color: #fff !important;
              border: none;
              color: #000 !important;
              height: 36px;
            }
            .inputcss .ant-input-group-addon {
              background-color: #fff !important;
              border: none;
              color: #000 !important;
            }
            .ant-input-affix-wrapper-focused {
              box-shadow: 0 0 0 2px rgb(0 0 0 / 5%) !important;
            }
            .ant-layout-sider-children .ant-input-group .ant-input,
            .ant-layout-sider-children .ant-input-search-button {
              border: 0px solid #eee !important;
              border-radius: 1px !important;
              color: #000 !important;
            }
            .inputcss .ant-select {
              color: #000 !important;
            }

            .inputcss input {
              background: #fff !important;
              color: #000 !important;
            }

            .leftMenuSider .lefttitle {
              background: #fff !important;
            }
            .inputcss .ant-select-arrow {
              color: #000 !important;
            }

            // 列表相关
            .ant-menu.ant-menu-dark,
            .ant-menu-dark .ant-menu-item,
            .ant-menu-submenu,
            .ant-layout-sider-children .ant-input-search-button svg {
              color: #000 !important;
            }

            .ant-menu-submenu-active,
            .ant-menu-item-active {
              color: #000 !important;
              background: #e7e7e7 !important;
            }

            .maxHeight800 .ant-menu-submenu-active,
            .maxHeight800 .ant-menu-item-active {
              color: #000 !important;
              background: #e7e7e7 !important;
            }

            .ant-menu.ant-menu-dark,
            .ant-menu-dark .ant-menu-sub,
            .ant-menu.ant-menu-dark .ant-menu-sub {
              color: #000 !important;
              background: #fff !important;
            }
            .ant-menu-dark.ant-menu-dark:not(.ant-menu-horizontal)
              .ant-menu-item-selected {
              background-color: #e7e7e7 !important;
            }

            .ant-menu-submenu-title:hover {
              color: #000 !important;
            }

            .foldbtn {
              border-left: 20px solid #1523351a !important;
            }
          `}),(0,n.tZ)(h.e,{style:{position:"relative",left:0,zIndex:9,background:ft?"#ffffff":"#1c2f47",width:M,borderRight:(ft?0:1)+"px solid #777777",height:"calc(100vh - 50px)"},enable:{right:!0},size:{width:M+"px"},onResize:(t,e,a,r)=>((t,e,a,r)=>{let o=q-0+(r.width-0);N(o)})(0,0,0,r),onResizeStart:()=>{},onResizeStop:(t,e,a,r)=>{let o=q-0+(r.width-0);A(o),(M<=130&&!O||M>130&&O)&&mt()},maxWidth:"550px",minWidth:O?"0px":"85px"},(0,n.tZ)(U,{className:"leftMenuSider",collapsible:!0,collapsed:O,trigger:null},(0,n.tZ)(_.Z,{dataAll:Y,Menuname:"chart",collapsed:O,handleChangeMenu:function(t){j(0),st(!1);const e=t.split("&&");B={chartId:parseInt(e[0]),pid:sessionStorage.getItem("chartGroup_id"),perm:e[4]},sessionStorage.setItem("chartIds",B.chartId.toString()),ct(t.split("&&")[2]),setTimeout((()=>{st(!0)}),500)},handleRemoveId:function(t=0){j(t)}})),(0,n.tZ)("span",{onClick:()=>mt(),className:"foldbtn"},O?(0,n.tZ)(m.default,{className:"foldbtnsvg"}):(0,n.tZ)(f.default,{className:"foldbtnsvg"}))),(0,n.tZ)(V,{style:{maxHeight:"calc(100vh - 50px)"}},0!=B.chartId&&0==Q?(0,n.tZ)("div",{style:{backgroundColor:"#FFFFFF",width:"100%",height:"50px",display:"flex",justifyContent:"space-between",padding:"5px 16px",fontSize:"16px",alignItems:"center"},className:"chartTopdiv"},(0,n.tZ)("div",{style:{fontSize:"18px",fontWeight:600}},""==it?(0,p.t)("Chart"):(0,n.tZ)(r.Fragment,null,it," ",(0,n.tZ)(R.Z,gt))),(0,n.tZ)("div",{style:{display:"flex",justifyContent:"space-between",alignItems:"center"}},B.perm>=4&&(0,n.tZ)(i.Z,{type:"primary",icon:(0,n.tZ)(g.default,null),onClick:()=>(()=>{const{chartId:t}=B;let e=`/explore/?slice_id=${t}`;window.location.href=(0,y.VU)(e)})()},(0,p.t)("Edit")),(0,n.tZ)("div",{style:{marginLeft:"10px"}},B.perm>=2&&(0,n.tZ)(c.Z,{overlay:(()=>{var t,e;const a=`#chart-id-${B.chartId}`,r=null==dt||null==(t=dt.form_data)?void 0:t.viz_type,o=null==dt||null==(e=dt.slice)?void 0:e.slice_name;return(0,n.tZ)(z.Z,{position:"chart-preview",selectorString:a,viz_type:r,downLoadTitle:o,slice:null==dt?void 0:dt.slice})})(),placement:"bottomLeft"},(0,n.tZ)("span",{style:{display:"block",borderRadius:"5px",width:"30px",height:"30px",textAlign:"center",border:"1px solid #5d9cec",cursor:"pointer"}},"..."))))):"",G&&(0,n.tZ)(C.Z,{onHide:X,onSave:K,show:!0,slice:G}),(0,n.tZ)(b.Z,{title:(0,p.t)("Please confirm"),description:(0,p.t)("Are you sure you want to delete the selected charts?"),onConfirm:function(t){u.Z.delete({endpoint:`/api/v1/chart/?q=${l().encode(t.map((({id:t})=>t)))}`}).then((({json:t={}})=>{D(),a(t.message)}),(0,x.v$)((t=>e((0,p.t)("There was an issue deleting the selected charts: %s",t)))))}},(e=>{const a=[];return ht&&a.push({key:"delete",name:(0,p.t)("Delete"),type:"danger",onSelect:e}),pt&&a.push({key:"export",name:(0,p.t)("Export"),type:"primary",onSelect:ut}),(0,n.tZ)(V,null,0!=B.chartId&&0==Q?(0,n.tZ)("div",{className:"chartcontentdiv"},(0,n.tZ)($,{show:nt,chartId:B.chartId,chartTitle:it,charts:t})):(0,n.tZ)("div",{style:{display:"flex",justifyContent:"center",alignItems:"center",height:"90vh"}},(0,n.tZ)("div",{style:{display:"flex",flexDirection:"column",alignItems:"center"}},(0,n.tZ)("img",{style:{width:"90px"},src:(0,y.VU)("/static/assets/images/emptyicon.png"),alt:""}),(0,n.tZ)("div",{style:{fontSize:"16px",color:"#BBBDBF",marginTop:"20px"}},(0,p.t)("Please select a chart on the left")))))})),(0,n.tZ)(T.Z,{resourceName:"chart",resourceLabel:(0,p.t)("chart"),passwordsNeededMessage:L,confirmOverwriteMessage:W,addDangerToast:e,addSuccessToast:a,onModelImport:()=>{tt(!1),D(),a((0,p.t)("Chart imported"))},show:J,onHide:()=>{tt(!1)},passwordFields:et,setPasswordFields:at}),rt&&(0,n.tZ)(Z.Z,null)))}))}}]);
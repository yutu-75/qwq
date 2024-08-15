(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[77230,75296],{325970:(e,t,a)=>{var n=a(863012),i=a(379095);e.exports=function(e,t){return n(e,t,(function(t,a){return i(e,a)}))}},478718:(e,t,a)=>{var n=a(325970),i=a(499021)((function(e,t){return null==e?{}:n(e,t)}));e.exports=i},762921:(e,t,a)=>{"use strict";a.d(t,{Z:()=>c});var n=a(667294),i=a(455867),o=a(34858),l=a(229487),r=a(211965);const s=(0,o.z)(),d=s?s.support:"https://superset.apache.org/docs/databases/installing-database-drivers",c=({errorMessage:e,showDbInstallInstructions:t})=>(0,r.tZ)(l.Z,{closable:!1,css:e=>(e=>r.iv`
  border: 1px solid ${e.colors.warning.light1};
  padding: ${4*e.gridUnit}px;
  margin: ${4*e.gridUnit}px 0;
  color: ${e.colors.warning.dark2};

  .ant-alert-message {
    margin: 0;
  }

  .ant-alert-description {
    font-size: ${e.typography.sizes.s+1}px;
    line-height: ${4*e.gridUnit}px;

    .ant-alert-icon {
      margin-right: ${2.5*e.gridUnit}px;
      font-size: ${e.typography.sizes.l+1}px;
      position: relative;
      top: ${e.gridUnit/4}px;
    }
  }
`)(e),type:"error",showIcon:!0,message:e,description:t?(0,r.tZ)(n.Fragment,null,(0,r.tZ)("br",null),(0,i.t)("Database driver for importing maybe not installed. Visit the Superset documentation page for installation instructions: "),(0,r.tZ)("a",{href:d,target:"_blank",rel:"noopener noreferrer",className:"additional-fields-alert-description"},(0,i.t)("here")),"."):""})},849576:(e,t,a)=>{"use strict";a.d(t,{Z:()=>h});var n=a(667294),i=a(751995),o=a(731293),l=a(211965);const r=i.iK.label`
  cursor: pointer;
  display: inline-block;
  margin-bottom: 0;
`,s=(0,i.iK)(o.Z.CheckboxHalf)`
  color: ${({theme:e})=>e.colors.primary.base};
  cursor: pointer;
`,d=(0,i.iK)(o.Z.CheckboxOff)`
  color: ${({theme:e})=>e.colors.grayscale.base};
  cursor: pointer;
`,c=(0,i.iK)(o.Z.CheckboxOn)`
  color: ${({theme:e})=>e.colors.primary.base};
  cursor: pointer;
`,u=i.iK.input`
  &[type='checkbox'] {
    cursor: pointer;
    opacity: 0;
    position: absolute;
    left: 3px;
    margin: 0;
    top: 4px;
  }
`,p=i.iK.div`
  cursor: pointer;
  display: inline-block;
  position: relative;
`,h=(0,n.forwardRef)((({indeterminate:e,id:t,checked:a,onChange:i,title:o="",labelText:h=""},m)=>{const g=(0,n.useRef)(),b=m||g;return(0,n.useEffect)((()=>{b.current.indeterminate=e}),[b,e]),(0,l.tZ)(n.Fragment,null,(0,l.tZ)(p,null,e&&(0,l.tZ)(s,null),!e&&a&&(0,l.tZ)(c,null),!e&&!a&&(0,l.tZ)(d,null),(0,l.tZ)(u,{name:t,id:t,type:"checkbox",ref:b,checked:a,onChange:i})),(0,l.tZ)(r,{title:o,htmlFor:t},h))}))},806646:(e,t,a)=>{"use strict";a.d(t,{Us:()=>ot,Gr:()=>lt,ZP:()=>dt});var n=a(478718),i=a.n(n),o=a(441609),l=a.n(o),r=a(175049),s=a(751995),d=a(455867),c=a(593185),u=a(667294),p=a(667496),h=a(961337),m=a(171262),g=a(49937),b=a(229487),v=a(774069),y=a(835932),f=a(731293);function Z(){return Z=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var a=arguments[t];for(var n in a)Object.prototype.hasOwnProperty.call(a,n)&&(e[n]=a[n])}return e},Z.apply(this,arguments)}const x={position:"absolute",bottom:0,left:0,height:0,overflow:"hidden","padding-top":0,"padding-bottom":0,border:"none"},_=["box-sizing","width","font-size","font-weight","font-family","font-style","letter-spacing","text-indent","white-space","word-break","overflow-wrap","padding-left","padding-right"];function w(e,t){for(;e&&t--;)e=e.previousElementSibling;return e}const C={basedOn:void 0,className:"",component:"div",ellipsis:"\u2026",maxLine:1,onReflow(){},text:"",trimRight:!0,winWidth:void 0},S=Object.keys(C);class $ extends u.Component{constructor(e){super(e),this.state={text:e.text,clamped:!1},this.units=[],this.maxLine=0,this.canvas=null}componentDidMount(){this.initCanvas(),this.reflow(this.props)}componentDidUpdate(e){e.winWidth!==this.props.winWidth&&this.copyStyleToCanvas(),this.props!==e&&this.reflow(this.props)}componentWillUnmount(){this.canvas.parentNode.removeChild(this.canvas)}setState(e,t){return"undefined"!==typeof e.clamped&&(this.clamped=e.clamped),super.setState(e,t)}initCanvas(){if(this.canvas)return;const e=this.canvas=document.createElement("div");e.className=`LinesEllipsis-canvas ${this.props.className}`,e.setAttribute("aria-hidden","true"),this.copyStyleToCanvas(),Object.keys(x).forEach((t=>{e.style[t]=x[t]})),document.body.appendChild(e)}copyStyleToCanvas(){const e=window.getComputedStyle(this.target);_.forEach((t=>{this.canvas.style[t]=e[t]}))}reflow(e){const t=e.basedOn||(/^[\x00-\x7F]+$/.test(e.text)?"words":"letters");switch(t){case"words":this.units=e.text.split(/\b|(?=\W)/);break;case"letters":this.units=Array.from(e.text);break;default:throw new Error(`Unsupported options basedOn: ${t}`)}this.maxLine=+e.maxLine||1,this.canvas.innerHTML=this.units.map((e=>`<span class='LinesEllipsis-unit'>${e}</span>`)).join("");const a=this.putEllipsis(this.calcIndexes()),n=a>-1,i={clamped:n,text:n?this.units.slice(0,a).join(""):e.text};this.setState(i,e.onReflow.bind(this,i))}calcIndexes(){const e=[0];let t=this.canvas.firstElementChild;if(!t)return e;let a=0,n=1,i=t.offsetTop;for(;(t=t.nextElementSibling)&&(t.offsetTop>i&&(n++,e.push(a),i=t.offsetTop),a++,!(n>this.maxLine)););return e}putEllipsis(e){if(e.length<=this.maxLine)return-1;const t=e[this.maxLine],a=this.units.slice(0,t),n=this.canvas.children[t].offsetTop;this.canvas.innerHTML=a.map(((e,t)=>`<span class='LinesEllipsis-unit'>${e}</span>`)).join("")+`<wbr><span class='LinesEllipsis-ellipsis'>${this.props.ellipsis}</span>`;const i=this.canvas.lastElementChild;let o=w(i,2);for(;o&&(i.offsetTop>n||i.offsetHeight>o.offsetHeight||i.offsetTop>o.offsetTop);)this.canvas.removeChild(o),o=w(i,2),a.pop();return a.length}isClamped(){return this.clamped}render(){const{text:e,clamped:t}=this.state,a=this.props,{component:n,ellipsis:i,trimRight:o,className:l}=a,r=function(e,t){if(null==e)return{};var a,n,i={},o=Object.keys(e);for(n=0;n<o.length;n++)a=o[n],t.indexOf(a)>=0||(i[a]=e[a]);return i}(a,["component","ellipsis","trimRight","className"]);return u.createElement(n,Z({className:`LinesEllipsis ${t?"LinesEllipsis--clamped":""} ${l}`,ref:e=>this.target=e},function(e,t){if(!e||"object"!==typeof e)return e;const a={};return Object.keys(e).forEach((n=>{t.indexOf(n)>-1||(a[n]=e[n])})),a}(r,S)),t&&o?e.replace(/[\s\uFEFF\xA0]+$/,""):e,u.createElement("wbr",null),t&&u.createElement("span",{className:"LinesEllipsis-ellipsis"},i))}}$.defaultProps=C;const k=$;var N=a(211965);const E=(0,s.iK)(y.Z)`
  height: auto;
  display: flex;
  flex-direction: column;
  padding: 0;
`,U=s.iK.div`
  padding: ${({theme:e})=>4*e.gridUnit}px;
  height: ${({theme:e})=>18*e.gridUnit}px;
  margin: ${({theme:e})=>3*e.gridUnit}px 0;

  .default-db-icon {
    font-size: 36px;
    color: ${({theme:e})=>e.colors.grayscale.base};
    margin-right: 0;
    span:first-of-type {
      margin-right: 0;
    }
  }

  &:first-of-type {
    margin-right: 0;
  }

  img {
    width: ${({theme:e})=>10*e.gridUnit}px;
    height: ${({theme:e})=>10*e.gridUnit}px;
    margin: 0;
    &:first-of-type {
      margin-right: 0;
    }
  }
  svg {
    &:first-of-type {
      margin-right: 0;
    }
  }
`,T=s.iK.div`
  max-height: calc(1.5em * 2);
  white-space: break-spaces;

  &:first-of-type {
    margin-right: 0;
  }

  .LinesEllipsis {
    &:first-of-type {
      margin-right: 0;
    }
  }
`,A=s.iK.div`
  padding: ${({theme:e})=>4*e.gridUnit}px 0;
  border-radius: 0 0 ${({theme:e})=>e.borderRadius}px
    ${({theme:e})=>e.borderRadius}px;
  background-color: ${({theme:e})=>e.colors.grayscale.light4};
  width: 100%;
  line-height: 1.5em;
  overflow: hidden;
  white-space: no-wrap;
  text-overflow: ellipsis;

  &:first-of-type {
    margin-right: 0;
  }
`,L=(0,s.iK)((({icon:e,altText:t,buttonText:a,...n})=>(0,N.tZ)(E,n,(0,N.tZ)(U,null,e&&(0,N.tZ)("img",{src:e,alt:t}),!e&&(0,N.tZ)(f.Z.DatabaseOutlined,{className:"default-db-icon","aria-label":"default-icon"})),(0,N.tZ)(A,null,(0,N.tZ)(T,null,(0,N.tZ)(k,{text:a,maxLine:"2",basedOn:"words",trimRight:!0}))))))`
  text-transform: none;
  background-color: ${({theme:e})=>e.colors.grayscale.light5};
  font-weight: ${({theme:e})=>e.typography.weights.normal};
  color: ${({theme:e})=>e.colors.grayscale.dark2};
  border: 1px solid ${({theme:e})=>e.colors.grayscale.light2};
  margin: 0;
  width: 100%;

  &:hover,
  &:focus {
    background-color: ${({theme:e})=>e.colors.grayscale.light5};
    color: ${({theme:e})=>e.colors.grayscale.dark2};
    border: 1px solid ${({theme:e})=>e.colors.grayscale.light2};
    box-shadow: 4px 4px 20px ${({theme:e})=>e.colors.grayscale.light2};
  }
`;var M,I,O=a(608272),q=a(414114),D=a(84367),F=a(272875),P=a(762921),R=a(34858),z=a(301483);!function(e){e.SQLALCHEMY_URI="sqlalchemy_form",e.DYNAMIC_FORM="dynamic_form"}(M||(M={})),function(e){e.GSheet="gsheets",e.Snowflake="snowflake"}(I||(I={}));var H=a(838703),j=a(294184),K=a.n(j),B=a(849576),Q=a(843700),J=a(794670);const V=N.iv`
  margin-bottom: 0;
`,G=s.iK.header`
  padding: ${({theme:e})=>2*e.gridUnit}px
    ${({theme:e})=>4*e.gridUnit}px;
  line-height: ${({theme:e})=>6*e.gridUnit}px;

  .helper-top {
    padding-bottom: 0;
    color: ${({theme:e})=>e.colors.grayscale.base};
    font-size: ${({theme:e})=>e.typography.sizes.s}px;
    margin: 0;
  }

  .subheader-text {
    line-height: ${({theme:e})=>4.25*e.gridUnit}px;
  }

  .helper-bottom {
    padding-top: 0;
    color: ${({theme:e})=>e.colors.grayscale.base};
    font-size: ${({theme:e})=>e.typography.sizes.s}px;
    margin: 0;
  }

  h4 {
    color: ${({theme:e})=>e.colors.grayscale.dark2};
    font-size: ${({theme:e})=>e.typography.sizes.l}px;
    margin: 0;
    padding: 0;
    line-height: ${({theme:e})=>8*e.gridUnit}px;
  }

  .select-db {
    padding-bottom: ${({theme:e})=>2*e.gridUnit}px;
    .helper {
      margin: 0;
    }

    h4 {
      margin: 0 0 ${({theme:e})=>4*e.gridUnit}px;
    }
  }
`,Y=N.iv`
  .ant-tabs-top {
    margin-top: 0;
  }
  .ant-tabs-top > .ant-tabs-nav {
    margin-bottom: 0;
  }
  .ant-tabs-tab {
    margin-right: 0;
  }
`,X=N.iv`
  .ant-modal-body {
    padding-left: 0;
    padding-right: 0;
    padding-top: 0;
  }
`,W=e=>N.iv`
  margin-bottom: ${5*e.gridUnit}px;
  svg {
    margin-bottom: ${.25*e.gridUnit}px;
  }
`,ee=e=>N.iv`
  padding-left: ${2*e.gridUnit}px;
`,te=e=>N.iv`
  padding: ${4*e.gridUnit}px ${4*e.gridUnit}px 0;
`,ae=e=>N.iv`
  .ant-select-dropdown {
    height: ${40*e.gridUnit}px;
  }

  .ant-modal-header {
    padding: ${4.5*e.gridUnit}px ${4*e.gridUnit}px
      ${4*e.gridUnit}px;
  }

  .ant-modal-close-x .close {
    color: ${e.colors.grayscale.dark1};
    opacity: 1;
  }

  .ant-modal-body {
    height: ${180.5*e.gridUnit}px;
  }

  .ant-modal-footer {
    height: ${16.25*e.gridUnit}px;
  }
`,ne=e=>N.iv`
  border: 1px solid ${e.colors.info.base};
  padding: ${4*e.gridUnit}px;
  margin: ${4*e.gridUnit}px 0;

  .ant-alert-message {
    color: ${e.colors.info.dark2};
    font-size: ${e.typography.sizes.m}px;
    font-weight: ${e.typography.weights.bold};
  }

  .ant-alert-description {
    color: ${e.colors.info.dark2};
    font-size: ${e.typography.sizes.m}px;
    line-height: ${5*e.gridUnit}px;

    a {
      text-decoration: underline;
    }

    .ant-alert-icon {
      margin-right: ${2.5*e.gridUnit}px;
      font-size: ${e.typography.sizes.l}px;
      position: relative;
      top: ${e.gridUnit/4}px;
    }
  }
`,ie=s.iK.div`
  ${({theme:e})=>N.iv`
    margin: 0 ${4*e.gridUnit}px -${4*e.gridUnit}px;
  `}
`,oe=e=>N.iv`
  .required {
    margin-left: ${e.gridUnit/2}px;
    color: ${e.colors.error.base};
  }

  .helper {
    display: block;
    padding: ${e.gridUnit}px 0;
    color: ${e.colors.grayscale.light1};
    font-size: ${e.typography.sizes.s}px;
    text-align: left;
  }
`,le=e=>N.iv`
  .form-group {
    margin-bottom: ${4*e.gridUnit}px;
    &-w-50 {
      display: inline-block;
      width: ${`calc(50% - ${4*e.gridUnit}px)`};
      & + .form-group-w-50 {
        margin-left: ${8*e.gridUnit}px;
      }
    }
  }
  .control-label {
    color: ${e.colors.grayscale.dark1};
    font-size: ${e.typography.sizes.s}px;
  }
  .helper {
    color: ${e.colors.grayscale.light1};
    font-size: ${e.typography.sizes.s}px;
    margin-top: ${1.5*e.gridUnit}px;
  }
  .ant-tabs-content-holder {
    overflow: auto;
    max-height: 480px;
  }
`,re=e=>N.iv`
  label {
    color: ${e.colors.grayscale.dark1};
    font-size: ${e.typography.sizes.s}px;
    margin-bottom: 0;
  }
`,se=s.iK.div`
  ${({theme:e})=>N.iv`
    margin-bottom: ${6*e.gridUnit}px;
    &.mb-0 {
      margin-bottom: 0;
    }
    &.mb-8 {
      margin-bottom: ${2*e.gridUnit}px;
    }

    .control-label {
      color: ${e.colors.grayscale.dark1};
      font-size: ${e.typography.sizes.s}px;
      margin-bottom: ${2*e.gridUnit}px;
    }

    &.extra-container {
      padding-top: ${2*e.gridUnit}px;
    }

    .input-container {
      display: flex;
      align-items: top;

      label {
        display: flex;
        margin-left: ${2*e.gridUnit}px;
        margin-top: ${.75*e.gridUnit}px;
        font-family: ${e.typography.families.sansSerif};
        font-size: ${e.typography.sizes.m}px;
      }

      i {
        margin: 0 ${e.gridUnit}px;
      }
    }

    input,
    textarea {
      flex: 1 1 auto;
    }

    textarea {
      height: 160px;
      resize: none;
    }

    input::placeholder,
    textarea::placeholder {
      color: ${e.colors.grayscale.light1};
    }

    textarea,
    input[type='text'],
    input[type='number'] {
      padding: ${1.5*e.gridUnit}px ${2*e.gridUnit}px;
      border-style: none;
      border: 1px solid ${e.colors.grayscale.light2};
      border-radius: ${e.gridUnit}px;

      &[name='name'] {
        flex: 0 1 auto;
        width: 40%;
      }
    }
    &.expandable {
      height: 0;
      overflow: hidden;
      transition: height 0.25s;
      margin-left: ${8*e.gridUnit}px;
      margin-bottom: 0;
      padding: 0;
      .control-label {
        margin-bottom: 0;
      }
      &.open {
        height: ${108}px;
        padding-right: ${5*e.gridUnit}px;
      }
    }
  `}
`,de=(0,s.iK)(J.Ad)`
  flex: 1 1 auto;
  border: 1px solid ${({theme:e})=>e.colors.grayscale.light2};
  border-radius: ${({theme:e})=>e.gridUnit}px;
`,ce=s.iK.div`
  padding-top: ${({theme:e})=>e.gridUnit}px;
  .input-container {
    padding-top: ${({theme:e})=>e.gridUnit}px;
    padding-bottom: ${({theme:e})=>e.gridUnit}px;
  }
  &.expandable {
    height: 0;
    overflow: hidden;
    transition: height 0.25s;
    margin-left: ${({theme:e})=>7*e.gridUnit}px;
    &.open {
      height: ${261}px;
      &.ctas-open {
        height: ${363}px;
      }
    }
  }
`,ue=s.iK.div`
  padding: 0 ${({theme:e})=>4*e.gridUnit}px;
  margin-top: ${({theme:e})=>6*e.gridUnit}px;
`,pe=e=>N.iv`
  font-weight: ${e.typography.weights.normal};
  text-transform: initial;
  padding-right: ${2*e.gridUnit}px;
`,he=e=>N.iv`
  font-size: ${3.5*e.gridUnit}px;
  font-weight: ${e.typography.weights.normal};
  text-transform: initial;
  padding-right: ${2*e.gridUnit}px;
`,me=s.iK.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 0px;

  .helper {
    color: ${({theme:e})=>e.colors.grayscale.base};
    font-size: ${({theme:e})=>e.typography.sizes.s}px;
    margin: 0px;
  }
`,ge=(s.iK.div`
  color: ${({theme:e})=>e.colors.grayscale.dark2};
  font-weight: ${({theme:e})=>e.typography.weights.bold};
  font-size: ${({theme:e})=>e.typography.sizes.m}px;
`,s.iK.div`
  color: ${({theme:e})=>e.colors.grayscale.dark1};
  font-size: ${({theme:e})=>e.typography.sizes.s}px;
`,s.iK.div`
  color: ${({theme:e})=>e.colors.grayscale.light1};
  font-size: ${({theme:e})=>e.typography.sizes.s}px;
  text-transform: uppercase;
`),be=s.iK.div`
  color: ${({theme:e})=>e.colors.grayscale.dark1};
  font-size: ${({theme:e})=>e.typography.sizes.l}px;
  font-weight: ${({theme:e})=>e.typography.weights.bold};
`,ve=s.iK.div`
  .catalog-type-select {
    margin: 0 0 20px;
  }

  .label-select {
    text-transform: uppercase;
    color: ${({theme:e})=>e.colors.grayscale.dark1};
    font-size: 11px;
    margin: 0 5px ${({theme:e})=>2*e.gridUnit}px;
  }

  .label-paste {
    color: ${({theme:e})=>e.colors.grayscale.light1};
    font-size: 11px;
    line-height: 16px;
  }

  .input-container {
    margin: ${({theme:e})=>7*e.gridUnit}px 0;
    display: flex;
    flex-direction: column;
}
  }
  .input-form {
    height: 100px;
    width: 100%;
    border: 1px solid ${({theme:e})=>e.colors.grayscale.light2};
    border-radius: ${({theme:e})=>e.gridUnit}px;
    resize: vertical;
    padding: ${({theme:e})=>1.5*e.gridUnit}px
      ${({theme:e})=>2*e.gridUnit}px;
    &::placeholder {
      color: ${({theme:e})=>e.colors.grayscale.light1};
    }
  }

  .input-container {
    .input-upload {
      display: none !important;
    }
    .input-upload-current {
      display: flex;
      justify-content: space-between;
    }
    .input-upload-btn {
      width: ${({theme:e})=>32*e.gridUnit}px
    }
  }`,ye=s.iK.div`
  .preferred {
    .superset-button {
      margin-left: 0;
    }
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    margin: ${({theme:e})=>4*e.gridUnit}px;
  }

  .preferred-item {
    width: 32%;
    margin-bottom: ${({theme:e})=>2.5*e.gridUnit}px;
  }

  .available {
    margin: ${({theme:e})=>4*e.gridUnit}px;
    .available-label {
      font-size: ${({theme:e})=>e.typography.sizes.l}px;
      font-weight: ${({theme:e})=>e.typography.weights.bold};
      margin: ${({theme:e})=>6*e.gridUnit}px 0;
    }
    .available-select {
      width: 100%;
    }
  }

  .label-available-select {
    text-transform: uppercase;
    font-size: ${({theme:e})=>e.typography.sizes.s}px;
  }

  .control-label {
    color: ${({theme:e})=>e.colors.grayscale.dark1};
    font-size: ${({theme:e})=>e.typography.sizes.s}px;
    margin-bottom: ${({theme:e})=>2*e.gridUnit}px;
  }
`,fe=(0,s.iK)(y.Z)`
  width: ${({theme:e})=>40*e.gridUnit}px;
`,Ze=s.iK.div`
  position: sticky;
  top: 0;
  z-index: ${({theme:e})=>e.zIndex.max};
  background: ${({theme:e})=>e.colors.grayscale.light5};
`,xe=s.iK.div`
  margin-bottom: 16px;

  .catalog-type-select {
    margin: 0 0 20px;
  }

  .gsheet-title {
    font-size: ${({theme:e})=>e.typography.sizes.l}px;
    font-weight: ${({theme:e})=>e.typography.weights.bold};
    margin: ${({theme:e})=>10*e.gridUnit}px 0 16px;
  }

  .catalog-label {
    margin: 0 0 7px;
  }

  .catalog-name {
    display: flex;
    .catalog-name-input {
      width: 95%;
      margin-bottom: 0px;
    }
  }

  .catalog-name-url {
    margin: 4px 0;
    width: 95%;
  }

  .catalog-add-btn {
    width: 95%;
  }
`,_e=s.iK.div`
  .ant-progress-inner {
    display: none;
  }

  .ant-upload-list-item-card-actions {
    display: none;
  }
`,we=({db:e,onInputChange:t,onTextChange:a,onEditorChange:n,onExtraInputChange:i,onExtraEditorChange:o})=>{var l,r,s;const c=!(null==e||!e.expose_in_sqllab),u=!!(null!=e&&e.allow_ctas||null!=e&&e.allow_cvas),p=null==e||null==(l=e.engine_information)?void 0:l.supports_file_upload,h=JSON.parse((null==e?void 0:e.extra)||"{}",((e,t)=>"engine_params"===e&&"object"===typeof t?JSON.stringify(t):t));return(0,N.tZ)(Q.Z,{expandIconPosition:"right",accordion:!0,css:e=>(e=>N.iv`
  .ant-collapse-header {
    padding-top: ${3.5*e.gridUnit}px;
    padding-bottom: ${2.5*e.gridUnit}px;

    .anticon.ant-collapse-arrow {
      top: calc(50% - ${6}px);
    }
    .helper {
      color: ${e.colors.grayscale.base};
    }
  }
  h4 {
    font-size: 16px;
    margin-top: 0;
    margin-bottom: ${e.gridUnit}px;
  }
  p.helper {
    margin-bottom: 0;
    padding: 0;
  }
`)(e)},(0,N.tZ)(Q.Z.Panel,{header:(0,N.tZ)("div",null,(0,N.tZ)("h4",null,(0,d.t)("SQL Lab")),(0,N.tZ)("p",{className:"helper"},(0,d.t)("Adjust how this database will interact with SQL Lab."))),key:"1"},(0,N.tZ)(se,{css:V},(0,N.tZ)("div",{className:"input-container"},(0,N.tZ)(B.Z,{id:"expose_in_sqllab",indeterminate:!1,checked:!(null==e||!e.expose_in_sqllab),onChange:t,labelText:(0,d.t)("Expose database in SQL Lab")}),(0,N.tZ)(O.Z,{tooltip:(0,d.t)("Allow this database to be queried in SQL Lab")})),(0,N.tZ)(ce,{className:K()("expandable",{open:c,"ctas-open":u})},(0,N.tZ)(se,{css:V},(0,N.tZ)("div",{className:"input-container"},(0,N.tZ)(B.Z,{id:"allow_ctas",indeterminate:!1,checked:!(null==e||!e.allow_ctas),onChange:t,labelText:(0,d.t)("Allow CREATE TABLE AS")}),(0,N.tZ)(O.Z,{tooltip:(0,d.t)("Allow creation of new tables based on queries")}))),(0,N.tZ)(se,{css:V},(0,N.tZ)("div",{className:"input-container"},(0,N.tZ)(B.Z,{id:"allow_cvas",indeterminate:!1,checked:!(null==e||!e.allow_cvas),onChange:t,labelText:(0,d.t)("Allow CREATE VIEW AS")}),(0,N.tZ)(O.Z,{tooltip:(0,d.t)("Allow creation of new views based on queries")})),(0,N.tZ)(se,{className:K()("expandable",{open:u})},(0,N.tZ)("div",{className:"control-label"},(0,d.t)("CTAS & CVAS SCHEMA")),(0,N.tZ)("div",{className:"input-container"},(0,N.tZ)("input",{type:"text",name:"force_ctas_schema",placeholder:(0,d.t)("Create or select schema..."),onChange:t,value:(null==e?void 0:e.force_ctas_schema)||""})),(0,N.tZ)("div",{className:"helper"},(0,d.t)("Force all tables and views to be created in this schema when clicking CTAS or CVAS in SQL Lab.")))),(0,N.tZ)(se,{css:V},(0,N.tZ)("div",{className:"input-container"},(0,N.tZ)(B.Z,{id:"allow_dml",indeterminate:!1,checked:!(null==e||!e.allow_dml),onChange:t,labelText:(0,d.t)("Allow DML")}),(0,N.tZ)(O.Z,{tooltip:(0,d.t)("Allow manipulation of the database using non-SELECT statements such as UPDATE, DELETE, CREATE, etc.")}))),(0,N.tZ)(se,{css:V},(0,N.tZ)("div",{className:"input-container"},(0,N.tZ)(B.Z,{id:"cost_estimate_enabled",indeterminate:!1,checked:!(null==h||!h.cost_estimate_enabled),onChange:i,labelText:(0,d.t)("Enable query cost estimation")}),(0,N.tZ)(O.Z,{tooltip:(0,d.t)("For Bigquery, Presto and Postgres, shows a button to compute cost before running a query.")}))),(0,N.tZ)(se,{css:V},(0,N.tZ)("div",{className:"input-container"},(0,N.tZ)(B.Z,{id:"allows_virtual_table_explore",indeterminate:!1,checked:!(null==h||!h.allows_virtual_table_explore),onChange:i,labelText:(0,d.t)("Allow this database to be explored")}),(0,N.tZ)(O.Z,{tooltip:(0,d.t)("When enabled, users are able to visualize SQL Lab results in Explore.")}))),(0,N.tZ)(se,null,(0,N.tZ)("div",{className:"input-container"},(0,N.tZ)(B.Z,{id:"disable_data_preview",indeterminate:!1,checked:!(null==h||!h.disable_data_preview),onChange:i,labelText:(0,d.t)("Disable SQL Lab data preview queries")}),(0,N.tZ)(O.Z,{tooltip:(0,d.t)("Disable data preview when fetching table metadata in SQL Lab.  Useful to avoid browser performance issues when using  databases with very wide tables.")})))))),(0,N.tZ)(Q.Z.Panel,{header:(0,N.tZ)("div",null,(0,N.tZ)("h4",null,(0,d.t)("Performance")),(0,N.tZ)("p",{className:"helper"},(0,d.t)("Adjust performance settings of this database."))),key:"2"},(0,N.tZ)(se,{className:"mb-8"},(0,N.tZ)("div",{className:"control-label"},(0,d.t)("Chart cache timeout")),(0,N.tZ)("div",{className:"input-container"},(0,N.tZ)("input",{type:"number",name:"cache_timeout",value:(null==e?void 0:e.cache_timeout)||"",placeholder:(0,d.t)("Enter duration in seconds"),onChange:t})),(0,N.tZ)("div",{className:"helper"},(0,d.t)("Duration (in seconds) of the caching timeout for charts of this database. A timeout of 0 indicates that the cache never expires. Note this defaults to the global timeout if undefined."))),(0,N.tZ)(se,null,(0,N.tZ)("div",{className:"control-label"},(0,d.t)("Schema cache timeout")),(0,N.tZ)("div",{className:"input-container"},(0,N.tZ)("input",{type:"number",name:"schema_cache_timeout",value:(null==h||null==(r=h.metadata_cache_timeout)?void 0:r.schema_cache_timeout)||"",placeholder:(0,d.t)("Enter duration in seconds"),onChange:i,"data-test":"schema-cache-timeout-test"})),(0,N.tZ)("div",{className:"helper"},(0,d.t)("Duration (in seconds) of the metadata caching timeout for schemas of this database. If left unset, the cache never expires."))),(0,N.tZ)(se,null,(0,N.tZ)("div",{className:"control-label"},(0,d.t)("Table cache timeout")),(0,N.tZ)("div",{className:"input-container"},(0,N.tZ)("input",{type:"number",name:"table_cache_timeout",value:(null==h||null==(s=h.metadata_cache_timeout)?void 0:s.table_cache_timeout)||"",placeholder:(0,d.t)("Enter duration in seconds"),onChange:i,"data-test":"table-cache-timeout-test"})),(0,N.tZ)("div",{className:"helper"},(0,d.t)("Duration (in seconds) of the metadata caching timeout for tables of this database. If left unset, the cache never expires. "))),(0,N.tZ)(se,{css:(0,N.iv)({no_margin_bottom:V},"","")},(0,N.tZ)("div",{className:"input-container"},(0,N.tZ)(B.Z,{id:"allow_run_async",indeterminate:!1,checked:!(null==e||!e.allow_run_async),onChange:t,labelText:(0,d.t)("Asynchronous query execution")}),(0,N.tZ)(O.Z,{tooltip:(0,d.t)("Operate the database in asynchronous mode, meaning that the queries are executed on remote workers as opposed to on the web server itself. This assumes that you have a Celery worker setup as well as a results backend. Refer to the installation docs for more information.")}))),(0,N.tZ)(se,{css:(0,N.iv)({no_margin_bottom:V},"","")},(0,N.tZ)("div",{className:"input-container"},(0,N.tZ)(B.Z,{id:"cancel_query_on_windows_unload",indeterminate:!1,checked:!(null==h||!h.cancel_query_on_windows_unload),onChange:i,labelText:(0,d.t)("Cancel query on window unload event")}),(0,N.tZ)(O.Z,{tooltip:(0,d.t)("Terminate running queries when browser window closed or navigated to another page. Available for Presto, Hive, MySQL, Postgres and Snowflake databases.")})))),(0,N.tZ)(Q.Z.Panel,{header:(0,N.tZ)("div",null,(0,N.tZ)("h4",null,(0,d.t)("Security")),(0,N.tZ)("p",{className:"helper"},(0,d.t)("Add extra connection information."))),key:"3"},(0,N.tZ)(se,null,(0,N.tZ)("div",{className:"control-label"},(0,d.t)("Secure extra")),(0,N.tZ)("div",{className:"input-container"},(0,N.tZ)(de,{name:"masked_encrypted_extra",value:(null==e?void 0:e.masked_encrypted_extra)||"",placeholder:(0,d.t)("Secure extra"),onChange:e=>n({json:e,name:"masked_encrypted_extra"}),width:"100%",height:"160px"})),(0,N.tZ)("div",{className:"helper"},(0,N.tZ)("div",null,(0,d.t)("JSON string containing additional connection configuration. This is used to provide connection information for systems like Hive, Presto and BigQuery which do not conform to the username:password syntax normally used by SQLAlchemy.")))),(0,N.tZ)(se,null,(0,N.tZ)("div",{className:"control-label"},(0,d.t)("Root certificate")),(0,N.tZ)("div",{className:"input-container"},(0,N.tZ)("textarea",{name:"server_cert",value:(null==e?void 0:e.server_cert)||"",placeholder:(0,d.t)("Enter CA_BUNDLE"),onChange:a})),(0,N.tZ)("div",{className:"helper"},(0,d.t)("Optional CA_BUNDLE contents to validate HTTPS requests. Only available on certain database engines."))),(0,N.tZ)(se,{css:p?{}:V},(0,N.tZ)("div",{className:"input-container"},(0,N.tZ)(B.Z,{id:"impersonate_user",indeterminate:!1,checked:!(null==e||!e.impersonate_user),onChange:t,labelText:(0,d.t)("Impersonate logged in user (Presto, Trino, Drill, Hive, and GSheets)")}),(0,N.tZ)(O.Z,{tooltip:(0,d.t)("If Presto or Trino, all the queries in SQL Lab are going to be executed as the currently logged on user who must have permission to run them. If Hive and hive.server2.enable.doAs is enabled, will run the queries as service account, but impersonate the currently logged on user via hive.server2.proxy.user property.")}))),p&&(0,N.tZ)(se,{css:null!=e&&e.allow_file_upload?{}:V},(0,N.tZ)("div",{className:"input-container"},(0,N.tZ)(B.Z,{id:"allow_file_upload",indeterminate:!1,checked:!(null==e||!e.allow_file_upload),onChange:t,labelText:(0,d.t)("Allow file uploads to database")}))),p&&!(null==e||!e.allow_file_upload)&&(0,N.tZ)(se,{css:V},(0,N.tZ)("div",{className:"control-label"},(0,d.t)("Schemas allowed for File upload")),(0,N.tZ)("div",{className:"input-container"},(0,N.tZ)("input",{type:"text",name:"schemas_allowed_for_file_upload",value:((null==h?void 0:h.schemas_allowed_for_file_upload)||[]).join(","),placeholder:"schema1,schema2",onChange:i})),(0,N.tZ)("div",{className:"helper"},(0,d.t)("A comma-separated list of schemas that files are allowed to upload to.")))),(0,N.tZ)(Q.Z.Panel,{header:(0,N.tZ)("div",null,(0,N.tZ)("h4",null,(0,d.t)("Other")),(0,N.tZ)("p",{className:"helper"},(0,d.t)("Additional settings."))),key:"4"},(0,N.tZ)(se,null,(0,N.tZ)("div",{className:"control-label"},(0,d.t)("Metadata Parameters")),(0,N.tZ)("div",{className:"input-container"},(0,N.tZ)(de,{name:"metadata_params",placeholder:(0,d.t)("Metadata Parameters"),onChange:e=>o({json:e,name:"metadata_params"}),width:"100%",height:"160px",defaultValue:Object.keys((null==h?void 0:h.metadata_params)||{}).length?null==h?void 0:h.metadata_params:""})),(0,N.tZ)("div",{className:"helper"},(0,N.tZ)("div",null,(0,d.t)("The metadata_params object gets unpacked into the sqlalchemy.MetaData call.")))),(0,N.tZ)(se,null,(0,N.tZ)("div",{className:"control-label"},(0,d.t)("Engine Parameters")),(0,N.tZ)("div",{className:"input-container"},(0,N.tZ)(de,{name:"engine_params",placeholder:(0,d.t)("Engine Parameters"),onChange:e=>o({json:e,name:"engine_params"}),width:"100%",height:"160px",defaultValue:Object.keys((null==h?void 0:h.engine_params)||{}).length?null==h?void 0:h.engine_params:""})),(0,N.tZ)("div",{className:"helper"},(0,N.tZ)("div",null,(0,d.t)("The engine_params object gets unpacked into the sqlalchemy.create_engine call.")))),(0,N.tZ)(se,null,(0,N.tZ)("div",{className:"control-label","data-test":"version-label-test"},(0,d.t)("Version")),(0,N.tZ)("div",{className:"input-container","data-test":"version-spinbutton-test"},(0,N.tZ)("input",{type:"number",name:"version",placeholder:(0,d.t)("Version number"),onChange:i,value:(null==h?void 0:h.version)||""})),(0,N.tZ)("div",{className:"helper"},(0,d.t)("Specify the database version. This should be used with Presto in order to enable query cost estimation.")))))};var Ce=a(208911);const Se=({db:e,onInputChange:t,testConnection:a,conf:n,testInProgress:i=!1,children:o})=>{let l,r;var s,c;Ce.Z?(l=null==(s=Ce.Z.DB_MODAL_SQLALCHEMY_FORM)?void 0:s.SQLALCHEMY_DOCS_URL,r=null==(c=Ce.Z.DB_MODAL_SQLALCHEMY_FORM)?void 0:c.SQLALCHEMY_DISPLAY_TEXT):(l="https://docs.sqlalchemy.org/en/13/core/engines.html",r="SQLAlchemy docs");return(0,N.tZ)(u.Fragment,null,(0,N.tZ)(se,null,(0,N.tZ)("div",{className:"control-label"},(0,d.t)("Display Name"),(0,N.tZ)("span",{className:"required"},"*")),(0,N.tZ)("div",{className:"input-container"},(0,N.tZ)("input",{type:"text",name:"database_name","data-test":"database-name-input",value:(null==e?void 0:e.database_name)||"",placeholder:(0,d.t)("Name your database"),onChange:t})),(0,N.tZ)("div",{className:"helper"},(0,d.t)("Pick a name to help you identify this database."))),(0,N.tZ)(se,null,(0,N.tZ)("div",{className:"control-label"},(0,d.t)("SQLAlchemy URI"),(0,N.tZ)("span",{className:"required"},"*")),(0,N.tZ)("div",{className:"input-container"},(0,N.tZ)("input",{type:"text",name:"sqlalchemy_uri","data-test":"sqlalchemy-uri-input",value:(null==e?void 0:e.sqlalchemy_uri)||"",autoComplete:"off",placeholder:(0,d.t)("dialect+driver://username:password@host:port/database"),onChange:t})),(0,N.tZ)("div",{className:"helper"},(0,d.t)("Refer to the")," ",(0,N.tZ)("a",{href:l||(null==n?void 0:n.SQLALCHEMY_DOCS_URL)||"",target:"_blank",rel:"noopener noreferrer"},r||(null==n?void 0:n.SQLALCHEMY_DISPLAY_TEXT)||"")," ",(0,d.t)("for more information on how to structure your URI."))),o,(0,N.tZ)(y.Z,{onClick:a,loading:i,cta:!0,buttonStyle:"link",css:e=>(e=>N.iv`
  width: 100%;
  border: 1px solid ${e.colors.primary.dark2};
  color: ${e.colors.primary.dark2};
  &:hover,
  &:focus {
    border: 1px solid ${e.colors.primary.dark1};
    color: ${e.colors.primary.dark1};
  }
`)(e)},(0,d.t)("Test connection")))};var $e=a(49238);const ke={account:{helpText:(0,d.t)("Copy the account name of that database you are trying to connect to."),placeholder:(0,d.t)("e.g. world_population")},warehouse:{placeholder:(0,d.t)("e.g. compute_wh"),className:"form-group-w-50"},role:{placeholder:(0,d.t)("e.g. AccountAdmin"),className:"form-group-w-50"}},Ne=({required:e,changeMethods:t,getValidation:a,validationErrors:n,db:i,field:o})=>{var l;return(0,N.tZ)(D.Z,{id:o,name:o,required:e,value:null==i||null==(l=i.parameters)?void 0:l[o],validationMethods:{onBlur:a},errorMessage:null==n?void 0:n[o],placeholder:ke[o].placeholder,helpText:ke[o].helpText,label:o,onChange:t.onParametersChange,className:ke[o].className||o})};var Ee,Ue=a(902857);!function(e){e[e.jsonUpload=0]="jsonUpload",e[e.copyPaste=1]="copyPaste"}(Ee||(Ee={}));const Te={gsheets:"service_account_info",bigquery:"credentials_info"};var Ae={name:"s5xdrg",styles:"display:flex;align-items:center"};const Le=({changeMethods:e,isEditMode:t,db:a,editNewDb:n})=>{var i,o,l;const[r,s]=(0,u.useState)(Ee.jsonUpload.valueOf()),[c,p]=(0,u.useState)(null),[h,m]=(0,u.useState)(!0),b="gsheets"===(null==a?void 0:a.engine)?!t&&!h:!t,v=t&&"{}"!==(null==a?void 0:a.masked_encrypted_extra),y=(null==a?void 0:a.engine)&&Te[a.engine],Z="object"===typeof(null==a||null==(i=a.parameters)?void 0:i[y])?JSON.stringify(null==a||null==(o=a.parameters)?void 0:o[y]):null==a||null==(l=a.parameters)?void 0:l[y];return(0,N.tZ)(ve,null,"gsheets"===(null==a?void 0:a.engine)&&(0,N.tZ)("div",{className:"catalog-type-select"},(0,N.tZ)(Ue.Z,{css:e=>(e=>N.iv`
  margin-bottom: ${2*e.gridUnit}px;
`)(e),required:!0},(0,d.t)("Type of Google Sheets allowed")),(0,N.tZ)(g.IZ,{style:{width:"100%"},defaultValue:v?"false":"true",onChange:e=>m("true"===e)},(0,N.tZ)(g.IZ.Option,{value:"true",key:1},(0,d.t)("Publicly shared sheets only")),(0,N.tZ)(g.IZ.Option,{value:"false",key:2},(0,d.t)("Public and privately shared sheets")))),b&&(0,N.tZ)(u.Fragment,null,(0,N.tZ)(Ue.Z,{required:!0},(0,d.t)("How do you want to enter service account credentials?")),(0,N.tZ)(g.IZ,{defaultValue:r,style:{width:"100%"},onChange:e=>s(e)},(0,N.tZ)(g.IZ.Option,{value:Ee.jsonUpload},(0,d.t)("Upload JSON file")),(0,N.tZ)(g.IZ.Option,{value:Ee.copyPaste},(0,d.t)("Copy and Paste JSON credentials")))),r===Ee.copyPaste||t||n?(0,N.tZ)("div",{className:"input-container"},(0,N.tZ)(Ue.Z,{required:!0},(0,d.t)("Service Account")),(0,N.tZ)("textarea",{className:"input-form",name:y,value:Z,onChange:e.onParametersChange,placeholder:(0,d.t)("Paste content of service credentials JSON file here")}),(0,N.tZ)("span",{className:"label-paste"},(0,d.t)("Copy and paste the entire service account .json file here"))):b&&(0,N.tZ)("div",{className:"input-container",css:e=>W(e)},(0,N.tZ)("div",{css:Ae},(0,N.tZ)(Ue.Z,{required:!0},(0,d.t)("Upload Credentials")),(0,N.tZ)(O.Z,{tooltip:(0,d.t)("Use the JSON file you automatically downloaded when creating your service account."),viewBox:"0 0 24 24"})),!c&&(0,N.tZ)(g.C0,{className:"input-upload-btn",onClick:()=>{var e,t;return null==(e=document)||null==(t=e.getElementById("selectedFile"))?void 0:t.click()}},(0,d.t)("Choose File")),c&&(0,N.tZ)("div",{className:"input-upload-current"},c,(0,N.tZ)(f.Z.DeleteFilled,{iconSize:"m",onClick:()=>{p(null),e.onParametersChange({target:{name:y,value:""}})}})),(0,N.tZ)("input",{id:"selectedFile",accept:".json",className:"input-upload",type:"file",onChange:async t=>{var a,n;let i;t.target.files&&(i=t.target.files[0]),p(null==(a=i)?void 0:a.name),e.onParametersChange({target:{type:null,name:y,value:await(null==(n=i)?void 0:n.text()),checked:!1}}),document.getElementById("selectedFile").value=null}})))},Me=["host","port","database","username","password","database_name","credentials_info","service_account_info","catalog","query","encryption","account","warehouse","role"],Ie={host:({required:e,changeMethods:t,getValidation:a,validationErrors:n,db:i})=>{var o;return(0,N.tZ)(D.Z,{id:"host",name:"host",value:null==i||null==(o=i.parameters)?void 0:o.host,required:e,hasTooltip:!0,tooltipText:(0,d.t)("This can be either an IP address (e.g. 127.0.0.1) or a domain name (e.g. mydatabase.com)."),validationMethods:{onBlur:a},errorMessage:null==n?void 0:n.host,placeholder:(0,d.t)("e.g. 127.0.0.1"),className:"form-group-w-50",label:(0,d.t)("Host"),onChange:t.onParametersChange})},port:({required:e,changeMethods:t,getValidation:a,validationErrors:n,db:i})=>{var o;return(0,N.tZ)(u.Fragment,null,(0,N.tZ)(D.Z,{id:"port",name:"port",type:"number",required:e,value:null==i||null==(o=i.parameters)?void 0:o.port,validationMethods:{onBlur:a},errorMessage:null==n?void 0:n.port,placeholder:(0,d.t)("e.g. 5432"),className:"form-group-w-50",label:(0,d.t)("Port"),onChange:t.onParametersChange}))},database:({required:e,changeMethods:t,getValidation:a,validationErrors:n,placeholder:i,db:o})=>{var l;return(0,N.tZ)(D.Z,{id:"database",name:"database",required:e,value:null==o||null==(l=o.parameters)?void 0:l.database,validationMethods:{onBlur:a},errorMessage:null==n?void 0:n.database,placeholder:null!=i?i:(0,d.t)("e.g. world_population"),label:(0,d.t)("Database name"),onChange:t.onParametersChange,helpText:(0,d.t)("Copy the name of the database you are trying to connect to.")})},username:({required:e,changeMethods:t,getValidation:a,validationErrors:n,db:i})=>{var o;return(0,N.tZ)(D.Z,{id:"username",name:"username",required:e,value:null==i||null==(o=i.parameters)?void 0:o.username,validationMethods:{onBlur:a},errorMessage:null==n?void 0:n.username,placeholder:(0,d.t)("e.g. Analytics"),label:(0,d.t)("Username"),onChange:t.onParametersChange})},password:({required:e,changeMethods:t,getValidation:a,validationErrors:n,db:i,isEditMode:o})=>{var l;return(0,N.tZ)(D.Z,{id:"password",name:"password",required:e,visibilityToggle:!o,value:null==i||null==(l=i.parameters)?void 0:l.password,validationMethods:{onBlur:a},errorMessage:null==n?void 0:n.password,placeholder:(0,d.t)("e.g. ********"),label:(0,d.t)("Password"),onChange:t.onParametersChange})},database_name:({changeMethods:e,getValidation:t,validationErrors:a,db:n})=>(0,N.tZ)(u.Fragment,null,(0,N.tZ)(D.Z,{id:"database_name",name:"database_name",required:!0,value:null==n?void 0:n.database_name,validationMethods:{onBlur:t},errorMessage:null==a?void 0:a.database_name,placeholder:"",label:(0,d.t)("Display Name"),onChange:e.onChange,helpText:(0,d.t)("Pick a nickname for how the database will display in Superset.")})),query:({required:e,changeMethods:t,getValidation:a,validationErrors:n,db:i})=>(0,N.tZ)(D.Z,{id:"query_input",name:"query_input",required:e,value:(null==i?void 0:i.query_input)||"",validationMethods:{onBlur:a},errorMessage:null==n?void 0:n.query,placeholder:(0,d.t)("e.g. param1=value1&param2=value2"),label:(0,d.t)("Additional Parameters"),onChange:t.onQueryChange,helpText:(0,d.t)("Add additional custom parameters")}),encryption:({isEditMode:e,changeMethods:t,db:a,sslForced:n})=>{var i;return(0,N.tZ)("div",{css:e=>W(e)},(0,N.tZ)(g.KU,{disabled:n&&!e,checked:(null==a||null==(i=a.parameters)?void 0:i.encryption)||n,onChange:e=>{t.onParametersChange({target:{type:"toggle",name:"encryption",checked:!0,value:e}})}}),(0,N.tZ)("span",{css:ee},"SSL"),(0,N.tZ)(O.Z,{tooltip:(0,d.t)('SSL Mode "require" will be used.'),placement:"right",viewBox:"0 -5 24 24"}))},credentials_info:Le,service_account_info:Le,catalog:({required:e,changeMethods:t,getValidation:a,validationErrors:n,db:i})=>{const o=(null==i?void 0:i.catalog)||[],l=n||{};return(0,N.tZ)(xe,null,(0,N.tZ)("h4",{className:"gsheet-title"},(0,d.t)("Connect Google Sheets as tables to this database")),(0,N.tZ)("div",null,null==o?void 0:o.map(((n,i)=>{var r,s;return(0,N.tZ)(u.Fragment,null,(0,N.tZ)(Ue.Z,{className:"catalog-label",required:!0},(0,d.t)("Google Sheet Name and URL")),(0,N.tZ)("div",{className:"catalog-name"},(0,N.tZ)(D.Z,{className:"catalog-name-input",required:e,validationMethods:{onBlur:a},errorMessage:null==(r=l[i])?void 0:r.name,placeholder:(0,d.t)("Enter a name for this sheet"),onChange:e=>{t.onParametersChange({target:{type:`catalog-${i}`,name:"name",value:e.target.value}})},value:n.name}),(null==o?void 0:o.length)>1&&(0,N.tZ)(f.Z.CloseOutlined,{css:e=>N.iv`
                    align-self: center;
                    background: ${e.colors.grayscale.light4};
                    margin: 5px 5px 8px 5px;

                    &.anticon > * {
                      line-height: 0;
                    }
                  `,iconSize:"m",onClick:()=>t.onRemoveTableCatalog(i)})),(0,N.tZ)(D.Z,{className:"catalog-name-url",required:e,validationMethods:{onBlur:a},errorMessage:null==(s=l[i])?void 0:s.url,placeholder:(0,d.t)("Paste the shareable Google Sheet URL here"),onChange:e=>t.onParametersChange({target:{type:`catalog-${i}`,name:"value",value:e.target.value}}),value:n.value}))})),(0,N.tZ)(fe,{className:"catalog-add-btn",onClick:()=>{t.onAddTableCatalog()}},"+ ",(0,d.t)("Add sheet"))))},warehouse:Ne,role:Ne,account:Ne},Oe=({dbModel:{parameters:e},onParametersChange:t,onChange:a,onQueryChange:n,onParametersUploadFileChange:i,onAddTableCatalog:o,onRemoveTableCatalog:l,validationErrors:r,getValidation:s,db:d,isEditMode:c=!1,sslForced:u,editNewDb:p})=>(0,N.tZ)($e.l0,null,(0,N.tZ)("div",{css:e=>[te,re(e)]},e&&Me.filter((t=>Object.keys(e.properties).includes(t)||"database_name"===t)).map((h=>{var m;return Ie[h]({required:null==(m=e.required)?void 0:m.includes(h),changeMethods:{onParametersChange:t,onChange:a,onQueryChange:n,onParametersUploadFileChange:i,onAddTableCatalog:o,onRemoveTableCatalog:l},validationErrors:r,getValidation:s,db:d,key:h,field:h,isEditMode:c,sslForced:u,editNewDb:p})})))),qe=(0,R.z)(),De=qe?qe.support:"https://superset.apache.org/docs/databases/installing-database-drivers",Fe={postgresql:"https://superset.apache.org/docs/databases/postgres",mssql:"https://superset.apache.org/docs/databases/sql-server",gsheets:"https://superset.apache.org/docs/databases/google-sheets"},Pe=({isLoading:e,isEditMode:t,useSqlAlchemyForm:a,hasConnectedDb:n,db:i,dbName:o,dbModel:l,editNewDb:r,fileList:s})=>{const c=s&&(null==s?void 0:s.length)>0,p=(0,N.tZ)(G,null,(0,N.tZ)(ge,null,null==i?void 0:i.backend),(0,N.tZ)(be,null,o)),h=(0,N.tZ)(G,null,(0,N.tZ)("p",{className:"helper-top"},(0,d.t)("STEP %(stepCurr)s OF %(stepLast)s",{stepCurr:2,stepLast:2})),(0,N.tZ)("h4",null,(0,d.t)("Enter Primary Credentials")),(0,N.tZ)("p",{className:"helper-bottom"},(0,d.t)("Need help? Learn how to connect your database")," ",(0,N.tZ)("a",{href:(null==qe?void 0:qe.default)||De,target:"_blank",rel:"noopener noreferrer"},(0,d.t)("here")),".")),m=(0,N.tZ)(Ze,null,(0,N.tZ)(G,null,(0,N.tZ)("p",{className:"helper-top"},(0,d.t)("STEP %(stepCurr)s OF %(stepLast)s",{stepCurr:3,stepLast:3})),(0,N.tZ)("h4",{className:"step-3-text"},(0,d.t)("Database connected")),(0,N.tZ)("p",{className:"subheader-text"},(0,d.t)("Create a dataset to begin visualizing your data as a chart or go to\n          SQL Lab to query your data.")))),g=(0,N.tZ)(Ze,null,(0,N.tZ)(G,null,(0,N.tZ)("p",{className:"helper-top"},(0,d.t)("STEP %(stepCurr)s OF %(stepLast)s",{stepCurr:2,stepLast:3})),(0,N.tZ)("h4",null,(0,d.t)("Enter the required %(dbModelName)s credentials",{dbModelName:l.name})),(0,N.tZ)("p",{className:"helper-bottom"},(0,d.t)("Need help? Learn more about")," ",(0,N.tZ)("a",{href:(b=null==i?void 0:i.engine,b?qe?qe[b]||qe.default:Fe[b]?Fe[b]:`https://superset.apache.org/docs/databases/${b}`:null),target:"_blank",rel:"noopener noreferrer"},(0,d.t)("connecting to %(dbModelName)s.",{dbModelName:l.name}),"."))));var b;const v=(0,N.tZ)(G,null,(0,N.tZ)("div",{className:"select-db"},(0,N.tZ)("p",{className:"helper-top"},(0,d.t)("STEP %(stepCurr)s OF %(stepLast)s",{stepCurr:1,stepLast:3})),(0,N.tZ)("h4",null,(0,d.t)("Select a database to connect")))),y=(0,N.tZ)(Ze,null,(0,N.tZ)(G,null,(0,N.tZ)("p",{className:"helper-top"},(0,d.t)("STEP %(stepCurr)s OF %(stepLast)s",{stepCurr:2,stepLast:2})),(0,N.tZ)("h4",null,(0,d.t)("Enter the required %(dbModelName)s credentials",{dbModelName:l.name})),(0,N.tZ)("p",{className:"helper-bottom"},c?s[0].name:"")));return c?y:e?(0,N.tZ)(u.Fragment,null):t?p:a?h:n&&!r?m:i||r?g:v};var Re=a(734265),ze=a(642419),He=a(287183),je=a(9875),Ke=a(432787),Be=a(931097);const Qe=s.iK.div`
  padding-top: ${({theme:e})=>2*e.gridUnit}px;
  label {
    color: ${({theme:e})=>e.colors.grayscale.base};
    text-transform: uppercase;
    margin-bottom: ${({theme:e})=>2*e.gridUnit}px;
  }
`,Je=(0,s.iK)(g.X2)`
  padding-bottom: ${({theme:e})=>2*e.gridUnit}px;
`,Ve=(0,s.iK)(g.qz.Item)`
  margin-bottom: 0 !important;
`,Ge=(0,s.iK)(Ke.Z.Password)`
  margin: ${({theme:e})=>`${e.gridUnit}px 0 ${2*e.gridUnit}px`};
`,Ye=({db:e,onSSHTunnelParametersChange:t,setSSHTunnelLoginMethod:a})=>{var n,i,o,l,r,s;const[c,p]=(0,u.useState)(lt.password);return(0,N.tZ)($e.l0,null,(0,N.tZ)(Je,{gutter:16},(0,N.tZ)(g.JX,{xs:24,md:12},(0,N.tZ)(Qe,null,(0,N.tZ)($e.lX,{htmlFor:"server_address",required:!0},(0,d.t)("SSH Host")),(0,N.tZ)(je.II,{name:"server_address",type:"text",placeholder:(0,d.t)("e.g. 127.0.0.1"),value:(null==e||null==(n=e.ssh_tunnel)?void 0:n.server_address)||"",onChange:t,"data-test":"ssh-tunnel-server_address-input"}))),(0,N.tZ)(g.JX,{xs:24,md:12},(0,N.tZ)(Qe,null,(0,N.tZ)($e.lX,{htmlFor:"server_port",required:!0},(0,d.t)("SSH Port")),(0,N.tZ)(je.II,{name:"server_port",type:"text",placeholder:(0,d.t)("22"),value:(null==e||null==(i=e.ssh_tunnel)?void 0:i.server_port)||"",onChange:t,"data-test":"ssh-tunnel-server_port-input"})))),(0,N.tZ)(Je,{gutter:16},(0,N.tZ)(g.JX,{xs:24},(0,N.tZ)(Qe,null,(0,N.tZ)($e.lX,{htmlFor:"username",required:!0},(0,d.t)("Username")),(0,N.tZ)(je.II,{name:"username",type:"text",placeholder:(0,d.t)("e.g. Analytics"),value:(null==e||null==(o=e.ssh_tunnel)?void 0:o.username)||"",onChange:t,"data-test":"ssh-tunnel-username-input"})))),(0,N.tZ)(Je,{gutter:16},(0,N.tZ)(g.JX,{xs:24},(0,N.tZ)(Qe,null,(0,N.tZ)($e.lX,{htmlFor:"use_password",required:!0},(0,d.t)("Login with")),(0,N.tZ)(Ve,{name:"use_password",initialValue:c},(0,N.tZ)(He.Y.Group,{onChange:({target:{value:e}})=>{p(e),a(e)}},(0,N.tZ)(He.Y,{value:lt.password,"data-test":"ssh-tunnel-use_password-radio"},(0,d.t)("Password")),(0,N.tZ)(He.Y,{value:lt.privateKey,"data-test":"ssh-tunnel-use_private_key-radio"},(0,d.t)("Private Key & Password"))))))),c===lt.password&&(0,N.tZ)(Je,{gutter:16},(0,N.tZ)(g.JX,{xs:24},(0,N.tZ)(Qe,null,(0,N.tZ)($e.lX,{htmlFor:"password",required:!0},(0,d.t)("SSH Password")),(0,N.tZ)(Ge,{name:"password",placeholder:(0,d.t)("e.g. ********"),value:(null==e||null==(l=e.ssh_tunnel)?void 0:l.password)||"",onChange:t,"data-test":"ssh-tunnel-password-input",iconRender:e=>e?(0,N.tZ)(Be.Z,{title:"Hide password."},(0,N.tZ)(Re.default,null)):(0,N.tZ)(Be.Z,{title:"Show password."},(0,N.tZ)(ze.default,null)),role:"textbox"})))),c===lt.privateKey&&(0,N.tZ)(u.Fragment,null,(0,N.tZ)(Je,{gutter:16},(0,N.tZ)(g.JX,{xs:24},(0,N.tZ)(Qe,null,(0,N.tZ)($e.lX,{htmlFor:"private_key",required:!0},(0,d.t)("Private Key")),(0,N.tZ)(je.Kx,{name:"private_key",placeholder:(0,d.t)("Paste Private Key here"),value:(null==e||null==(r=e.ssh_tunnel)?void 0:r.private_key)||"",onChange:t,"data-test":"ssh-tunnel-private_key-input",rows:4})))),(0,N.tZ)(Je,{gutter:16},(0,N.tZ)(g.JX,{xs:24},(0,N.tZ)(Qe,null,(0,N.tZ)($e.lX,{htmlFor:"private_key_password",required:!0},(0,d.t)("Private Key Password")),(0,N.tZ)(Ge,{name:"private_key_password",placeholder:(0,d.t)("e.g. ********"),value:(null==e||null==(s=e.ssh_tunnel)?void 0:s.private_key_password)||"",onChange:t,"data-test":"ssh-tunnel-private_key_password-input",iconRender:e=>e?(0,N.tZ)(Be.Z,{title:"Hide password."},(0,N.tZ)(Re.default,null)):(0,N.tZ)(Be.Z,{title:"Show password."},(0,N.tZ)(ze.default,null)),role:"textbox"}))))))},Xe=({isEditMode:e,dbFetched:t,useSSHTunneling:a,setUseSSHTunneling:n,setDB:i,isSSHTunneling:o})=>o?(0,N.tZ)("div",{css:e=>W(e)},(0,N.tZ)(g.KU,{disabled:e&&!l()(null==t?void 0:t.ssh_tunnel),checked:a,onChange:e=>{n(e),e||i({type:ot.removeSSHTunnelConfig})},"data-test":"ssh-tunnel-switch"}),(0,N.tZ)("span",{css:ee},(0,d.t)("SSH Tunnel")),(0,N.tZ)(O.Z,{tooltip:(0,d.t)("SSH Tunnel configuration parameters"),placement:"right",viewBox:"0 -5 24 24"})):null,We=(0,r.I)(),et=JSON.stringify({allows_virtual_table_explore:!0}),tt={[I.GSheet]:{message:"Why do I need to create a database?",description:"To begin using your Google Sheets, you need to create a database first. Databases are used as a way to identify your data so that it can be queried and visualized. This database will hold all of your individual Google Sheets you choose to connect here."}},at=(0,s.iK)(m.ZP)`
  .ant-tabs-content {
    display: flex;
    width: 100%;
    overflow: inherit;

    & > .ant-tabs-tabpane {
      position: relative;
    }
  }
`,nt=s.iK.div`
  ${({theme:e})=>`\n    margin: ${8*e.gridUnit}px ${4*e.gridUnit}px;\n  `};
`,it=s.iK.div`
  ${({theme:e})=>`\n    padding: 0px ${4*e.gridUnit}px;\n  `};
`;var ot,lt;!function(e){e[e.addTableCatalogSheet=0]="addTableCatalogSheet",e[e.configMethodChange=1]="configMethodChange",e[e.dbSelected=2]="dbSelected",e[e.editorChange=3]="editorChange",e[e.extraEditorChange=4]="extraEditorChange",e[e.extraInputChange=5]="extraInputChange",e[e.fetched=6]="fetched",e[e.inputChange=7]="inputChange",e[e.parametersChange=8]="parametersChange",e[e.queryChange=9]="queryChange",e[e.removeTableCatalogSheet=10]="removeTableCatalogSheet",e[e.reset=11]="reset",e[e.textChange=12]="textChange",e[e.parametersSSHTunnelChange=13]="parametersSSHTunnelChange",e[e.setSSHTunnelLoginMethod=14]="setSSHTunnelLoginMethod",e[e.removeSSHTunnelConfig=15]="removeSSHTunnelConfig"}(ot||(ot={})),function(e){e[e.password=0]="password",e[e.privateKey=1]="privateKey"}(lt||(lt={}));const rt=s.iK.div`
  margin-bottom: ${({theme:e})=>3*e.gridUnit}px;
  margin-left: ${({theme:e})=>3*e.gridUnit}px;
`;function st(e,t){var a,n,o,l;const r={...e||{}};let s,d,c={},u="";const p=JSON.parse(r.extra||"{}");switch(t.type){case ot.extraEditorChange:try{d=JSON.parse(t.payload.json||"{}")}catch(e){d=t.payload.json}return{...r,extra:JSON.stringify({...p,[t.payload.name]:d})};case ot.extraInputChange:return"schema_cache_timeout"===t.payload.name||"table_cache_timeout"===t.payload.name?{...r,extra:JSON.stringify({...p,metadata_cache_timeout:{...null==p?void 0:p.metadata_cache_timeout,[t.payload.name]:t.payload.value}})}:"schemas_allowed_for_file_upload"===t.payload.name?{...r,extra:JSON.stringify({...p,schemas_allowed_for_file_upload:(t.payload.value||"").split(",").filter((e=>""!==e))})}:"http_path"===t.payload.name?{...r,extra:JSON.stringify({...p,engine_params:{connect_args:{[t.payload.name]:null==(h=t.payload.value)?void 0:h.trim()}}})}:{...r,extra:JSON.stringify({...p,[t.payload.name]:"checkbox"===t.payload.type?t.payload.checked:t.payload.value})};var h;case ot.inputChange:return"checkbox"===t.payload.type?{...r,[t.payload.name]:t.payload.checked}:{...r,[t.payload.name]:t.payload.value};case ot.parametersChange:if(null!=(a=t.payload.type)&&a.startsWith("catalog")&&void 0!==r.catalog){var m;const e=[...r.catalog],a=null==(m=t.payload.type)?void 0:m.split("-")[1],n=e[a]||{};return n[t.payload.name]=t.payload.value,e.splice(parseInt(a,10),1,n),s=e.reduce(((e,t)=>{const a={...e};return a[t.name]=t.value,a}),{}),{...r,catalog:e,parameters:{...r.parameters,catalog:s}}}return{...r,parameters:{...r.parameters,[t.payload.name]:t.payload.value}};case ot.parametersSSHTunnelChange:return{...r,ssh_tunnel:{...r.ssh_tunnel,[t.payload.name]:t.payload.value}};case ot.setSSHTunnelLoginMethod:{let e={};var g,b,v;return null!=r&&r.ssh_tunnel&&(e=i()(r.ssh_tunnel,["id","server_address","server_port","username"])),t.payload.login_method===lt.privateKey?{...r,ssh_tunnel:{private_key:null==r||null==(g=r.ssh_tunnel)?void 0:g.private_key,private_key_password:null==r||null==(b=r.ssh_tunnel)?void 0:b.private_key_password,...e}}:t.payload.login_method===lt.password?{...r,ssh_tunnel:{password:null==r||null==(v=r.ssh_tunnel)?void 0:v.password,...e}}:{...r}}case ot.removeSSHTunnelConfig:return{...r,ssh_tunnel:void 0};case ot.addTableCatalogSheet:return void 0!==r.catalog?{...r,catalog:[...r.catalog,{name:"",value:""}]}:{...r,catalog:[{name:"",value:""}]};case ot.removeTableCatalogSheet:return null==(n=r.catalog)||n.splice(t.payload.indexToDelete,1),{...r};case ot.editorChange:return{...r,[t.payload.name]:t.payload.json};case ot.queryChange:return{...r,parameters:{...r.parameters,query:Object.fromEntries(new URLSearchParams(t.payload.value))},query_input:t.payload.value};case ot.textChange:return{...r,[t.payload.name]:t.payload.value};case ot.fetched:if(c=(null==(o=t.payload)||null==(l=o.parameters)?void 0:l.query)||{},u=Object.entries(c).map((([e,t])=>`${e}=${t}`)).join("&"),t.payload.masked_encrypted_extra&&t.payload.configuration_method===M.DYNAMIC_FORM){var y;const e=null==(y={...JSON.parse(t.payload.extra||"{}")}.engine_params)?void 0:y.catalog,a=Object.entries(e||{}).map((([e,t])=>({name:e,value:t})));return{...t.payload,engine:t.payload.backend||r.engine,configuration_method:t.payload.configuration_method,catalog:a,parameters:{...t.payload.parameters||r.parameters,catalog:e},query_input:u}}return{...t.payload,masked_encrypted_extra:t.payload.masked_encrypted_extra||"",engine:t.payload.backend||r.engine,configuration_method:t.payload.configuration_method,parameters:t.payload.parameters||r.parameters,ssh_tunnel:t.payload.ssh_tunnel||r.ssh_tunnel,query_input:u};case ot.dbSelected:return{...t.payload,extra:et,expose_in_sqllab:!0};case ot.configMethodChange:return{...t.payload};case ot.reset:default:return null}}const dt=(0,q.ZP)((({addDangerToast:e,addSuccessToast:t,onDatabaseAdd:a,onHide:n,show:i,databaseId:o,dbEngine:r,history:s})=>{var f,Z,x,_,w;const[C,S]=(0,u.useReducer)(st,null),{state:{loading:$,resource:k,error:E},fetchResource:U,createResource:T,updateResource:A,clearError:q}=(0,R.LE)("database",(0,d.t)("database"),e),[j,K]=(0,u.useState)("1"),[B,Q]=(0,R.cb)(),[J,V,G]=(0,R.h1)(),[ee,re]=(0,u.useState)(!1),[se,de]=(0,u.useState)(!1),[ce,ge]=(0,u.useState)(""),[be,ve]=(0,u.useState)(!1),[xe,Ce]=(0,u.useState)(!1),[$e,ke]=(0,u.useState)(!1),[Ne,Ee]=(0,u.useState)({}),[Ue,Te]=(0,u.useState)(!1),[Ae,Le]=(0,u.useState)([]),[Me,Ie]=(0,u.useState)(!1),[qe,Fe]=(0,u.useState)(),[Re,ze]=(0,u.useState)([]),He=null!=(f=We.get("ssh_tunnel.form.switch"))?f:Xe,[je,Ke]=(0,u.useState)(!1),Be=(0,z.c)(),Qe=(0,R.rM)(),Je=(0,R.jb)(),Ve=!!o,Ge=(0,c.c)(c.T.FORCE_DATABASE_CONNECTIONS_SSL),et=null==B||null==(Z=B.databases)||null==(x=Z.find((e=>e.backend===(null==C?void 0:C.engine)||e.engine===(null==C?void 0:C.engine))))||null==(_=x.engine_information)?void 0:_.disable_ssh_tunneling,lt=(0,c.c)(c.T.SSH_TUNNELING)&&!et,dt=Je||!(null==C||!C.engine||!tt[C.engine]),ct=(null==C?void 0:C.configuration_method)===M.SQLALCHEMY_URI,ut=Ve||ct,pt=J||E,ht=(null==B||null==(w=B.databases)?void 0:w.find((e=>e.engine===(Ve?null==C?void 0:C.backend:null==C?void 0:C.engine))))||{},mt=e=>{if("database"===e)return(null==C?void 0:C.engine)===I.Snowflake?(0,d.t)("e.g. xy12345.us-east-2.aws"):(0,d.t)("e.g. world_population")},gt=()=>{S({type:ot.reset}),re(!1),G(null),q(),ve(!1),Le([]),Ie(!1),Fe(""),ze([]),Ee({}),Te(!1),Ke(!1),n()},{state:{alreadyExists:bt,passwordsNeeded:vt,loading:yt,failed:ft},importResource:Zt}=(0,R.PW)("database",(0,d.t)("database"),(e=>{Fe(e)})),xt=(e,t)=>{S({type:e,payload:t})},_t=async()=>{var e;const n={...C||{}};if(n.configuration_method===M.DYNAMIC_FORM){var i,o;null!=n&&null!=(i=n.parameters)&&i.catalog&&(n.extra=JSON.stringify({...JSON.parse(n.extra||"{}"),engine_params:{catalog:n.parameters.catalog}})),null!=n&&n.catalog&&0===n.catalog.length&&delete n.catalog,Ce(!0);const e=await V(n,!0);if(J&&!l()(J)||e)return void Ce(!1);Ce(!1);const t=Ve?null==(o=n.parameters_schema)?void 0:o.properties:null==ht?void 0:ht.parameters.properties,a=JSON.parse(n.masked_encrypted_extra||"{}");Object.keys(t||{}).forEach((e=>{var i,o,l,r;t[e]["x-encrypted-extra"]&&null!=(i=n.parameters)&&i[e]&&("object"===typeof(null==(o=n.parameters)?void 0:o[e])?(a[e]=null==(l=n.parameters)?void 0:l[e],n.parameters[e]=JSON.stringify(n.parameters[e])):a[e]=JSON.parse((null==(r=n.parameters)?void 0:r[e])||"{}"))})),n.masked_encrypted_extra=JSON.stringify(a),n.engine===I.GSheet&&(n.impersonate_user=!0)}if(null!=n&&null!=(e=n.parameters)&&e.catalog&&(n.extra=JSON.stringify({...JSON.parse(n.extra||"{}"),engine_params:{catalog:n.parameters.catalog}})),Ce(!0),null!=C&&C.id){C.database_id=C.database_id?C.database_id:C.id;await A(C.database_id,n,n.configuration_method===M.DYNAMIC_FORM)&&(a&&a(1),be||(gt(),t((0,d.t)("Database settings updated"))))}else if(C){n.group_id=sessionStorage.getItem("newsqldatabaseid"),n.configuration_method=M.DYNAMIC_FORM;await T(n,n.configuration_method===M.DYNAMIC_FORM)&&(re(!0),a&&a(1),ut&&(gt(),t((0,d.t)("Database connected"))))}else{if(Ie(!0),!(Ae[0].originFileObj instanceof File))return;await Zt(Ae[0].originFileObj,Ne,Ue)&&(a&&a(1),gt(),t((0,d.t)("Database connected")))}de(!0),ve(!1),Ce(!1)},wt=e=>{if("Other"===e)S({type:ot.dbSelected,payload:{database_name:e,configuration_method:M.SQLALCHEMY_URI,engine:void 0,engine_information:{supports_file_upload:!0}}});else{const t=null==B?void 0:B.databases.filter((t=>t.name===e))[0],{engine:a,parameters:n,engine_information:i,default_driver:o}=t,l=void 0!==n;S({type:ot.dbSelected,payload:{database_name:e,engine:a,configuration_method:l?M.DYNAMIC_FORM:M.SQLALCHEMY_URI,engine_information:i,driver:o}}),a===I.GSheet&&S({type:ot.addTableCatalogSheet})}},Ct=()=>{k&&U(k.database_id),de(!1),ve(!0)},St=()=>{be&&re(!1),Me&&Ie(!1),ft&&(Ie(!1),Fe(""),ze([]),Ee({})),S({type:ot.reset}),Le([])},$t=()=>C?!ee||be?(0,N.tZ)(u.Fragment,null,(0,N.tZ)(fe,{key:"back",onClick:St},(0,d.t)("Back")),(0,N.tZ)(fe,{key:"submit",buttonStyle:"primary",onClick:_t,loading:xe},(0,d.t)("Connect"))):(0,N.tZ)(u.Fragment,null,(0,N.tZ)(fe,{key:"back",onClick:Ct},(0,d.t)("Back")),(0,N.tZ)(fe,{key:"submit",buttonStyle:"primary",onClick:_t,"data-test":"modal-confirm-button",loading:xe},(0,d.t)("Finish"))):Me?(0,N.tZ)(u.Fragment,null,(0,N.tZ)(fe,{key:"back",onClick:St},(0,d.t)("Back")),(0,N.tZ)(fe,{key:"submit",buttonStyle:"primary",onClick:_t,disabled:!!(yt||bt.length&&!Ue||vt.length&&"{}"===JSON.stringify(Ne)),loading:xe},(0,d.t)("Connect"))):(0,N.tZ)(u.Fragment,null),kt=(0,u.useRef)(!0);(0,u.useEffect)((()=>{kt.current?kt.current=!1:yt||bt.length||vt.length||xe||ft||(gt(),t((0,d.t)("Database connected")))}),[bt,vt,yt,ft]),(0,u.useEffect)((()=>{i&&(K("1"),Ce(!0),Q()),o&&i&&Ve&&o&&($||U(o).catch((t=>e((0,d.t)("Sorry there was an error fetching database information: %s",t.message)))))}),[i,o]),(0,u.useEffect)((()=>{k&&(S({type:ot.fetched,payload:k}),ge(k.database_name))}),[k]),(0,u.useEffect)((()=>{xe&&Ce(!1),B&&r&&wt(r)}),[B]),(0,u.useEffect)((()=>{Me&&document.getElementsByClassName("ant-upload-list-item-name")[0].scrollIntoView()}),[Me]),(0,u.useEffect)((()=>{ze([...vt])}),[vt]),(0,u.useEffect)((()=>{C&&lt&&Ke(!l()(null==C?void 0:C.ssh_tunnel))}),[C,lt]);const Nt=()=>qe?(0,N.tZ)(ie,null,(0,N.tZ)(P.Z,{errorMessage:qe,showDbInstallInstructions:Re.length>0})):null,Et=e=>{var t,a;const n=null!=(t=null==(a=e.currentTarget)?void 0:a.value)?t:"";Te(n.toUpperCase()===(0,d.t)("OVERWRITE"))},Ut=()=>bt.length?(0,N.tZ)(u.Fragment,null,(0,N.tZ)(ie,null,(0,N.tZ)(b.Z,{closable:!1,css:e=>(e=>N.iv`
  border: 1px solid ${e.colors.warning.light1};
  padding: ${4*e.gridUnit}px;
  margin: ${4*e.gridUnit}px 0;
  color: ${e.colors.warning.dark2};

  .ant-alert-message {
    margin: 0;
  }

  .ant-alert-description {
    font-size: ${e.typography.sizes.s+1}px;
    line-height: ${4*e.gridUnit}px;

    .ant-alert-icon {
      margin-right: ${2.5*e.gridUnit}px;
      font-size: ${e.typography.sizes.l+1}px;
      position: relative;
      top: ${e.gridUnit/4}px;
    }
  }
`)(e),type:"warning",showIcon:!0,message:"",description:(0,d.t)("You are importing one or more databases that already exist. Overwriting might cause you to lose some of your work. Are you sure you want to overwrite?")})),(0,N.tZ)(D.Z,{id:"confirm_overwrite",name:"confirm_overwrite",required:!0,validationMethods:{onBlur:()=>{}},errorMessage:null==J?void 0:J.confirm_overwrite,label:(0,d.t)('Type "%s" to confirm',(0,d.t)("OVERWRITE")),onChange:Et,css:te})):null,Tt=()=>{let e=[];var t;return l()(E)?l()(J)||"GENERIC_DB_ENGINE_ERROR"!==(null==J?void 0:J.error_type)||(e=[(null==J?void 0:J.description)||(null==J?void 0:J.message)]):e="object"===typeof E?Object.values(E):"string"===typeof E?[E]:[],e.length?(0,N.tZ)(nt,null,(0,N.tZ)(F.Z,{title:(0,d.t)("Database Creation Error"),description:(0,d.t)('We are unable to connect to your database. Click "See more" for database-provided information that may help troubleshoot the issue.'),subtitle:(null==(t=e)?void 0:t[0])||(null==J?void 0:J.description),copyText:null==J?void 0:J.description})):(0,N.tZ)(u.Fragment,null)},At=()=>(0,N.tZ)(Ye,{db:C,onSSHTunnelParametersChange:({target:e})=>xt(ot.parametersSSHTunnelChange,{type:e.type,name:e.name,value:e.value}),setSSHTunnelLoginMethod:e=>S({type:ot.setSSHTunnelLoginMethod,payload:{login_method:e}})}),Lt=()=>(0,N.tZ)(u.Fragment,null,(0,N.tZ)(Oe,{isEditMode:Ve,db:C,sslForced:Ge,dbModel:ht,onAddTableCatalog:()=>{S({type:ot.addTableCatalogSheet})},onQueryChange:({target:e})=>xt(ot.queryChange,{name:e.name,value:e.value}),onExtraInputChange:({target:e})=>xt(ot.extraInputChange,{name:e.name,value:e.value}),onRemoveTableCatalog:e=>{S({type:ot.removeTableCatalogSheet,payload:{indexToDelete:e}})},onParametersChange:({target:e})=>xt(ot.parametersChange,{type:e.type,name:e.name,checked:e.checked,value:e.value}),onChange:({target:e})=>xt(ot.textChange,{name:e.name,value:e.value}),getValidation:()=>V(C),validationErrors:J,getPlaceholder:mt}),(0,N.tZ)(it,null,(0,N.tZ)(He,{isEditMode:Ve,dbFetched:k,disableSSHTunnelingForEngine:et,useSSHTunneling:je,setUseSSHTunneling:Ke,setDB:S,isSSHTunneling:lt})),je&&(0,N.tZ)(it,null,At()));if(Ae.length>0&&(bt.length||Re.length))return(0,N.tZ)(v.Z,{css:e=>[X,ae(e),oe(e),le(e)],name:"database",onHandledPrimaryAction:_t,onHide:gt,primaryButtonName:(0,d.t)("Connect"),width:"500px",centered:!0,show:i,title:(0,N.tZ)("h4",null,(0,d.t)("Connect a database")),footer:$t()},(0,N.tZ)(Pe,{isLoading:xe,isEditMode:Ve,useSqlAlchemyForm:ct,hasConnectedDb:ee,db:C,dbName:ce,dbModel:ht,fileList:Ae}),Re.length?Re.map((e=>(0,N.tZ)(u.Fragment,null,(0,N.tZ)(ie,null,(0,N.tZ)(b.Z,{closable:!1,css:e=>ne(e),type:"info",showIcon:!0,message:"Database passwords",description:(0,d.t)('The passwords for the databases below are needed in order to import them. Please note that the "Secure Extra" and "Certificate" sections of the database configuration are not present in explore files and should be added manually after the import if they are needed.')})),(0,N.tZ)(D.Z,{id:"password_needed",name:"password_needed",required:!0,value:Ne[e],onChange:t=>Ee({...Ne,[e]:t.target.value}),validationMethods:{onBlur:()=>{}},errorMessage:null==J?void 0:J.password_needed,label:(0,d.t)("%s PASSWORD",e.slice(10)),css:te})))):null,Ut(),Nt());const Mt=Ve?(e=>(0,N.tZ)(u.Fragment,null,(0,N.tZ)(fe,{key:"close",onClick:gt},(0,d.t)("Close")),(0,N.tZ)(fe,{key:"submit",buttonStyle:"primary",onClick:_t,disabled:null==e?void 0:e.is_managed_externally,loading:xe,tooltip:null!=e&&e.is_managed_externally?(0,d.t)("This database is managed externally, and can't be edited in Superset"):""},(0,d.t)("Finish"))))(C):$t();return ut?(0,N.tZ)(v.Z,{css:e=>[Y,X,ae(e),oe(e),le(e)],name:"database","data-test":"database-modal",onHandledPrimaryAction:_t,onHide:gt,primaryButtonName:Ve?(0,d.t)("Save"):(0,d.t)("Connect"),width:"500px",centered:!0,show:i,title:(0,N.tZ)("h4",null,Ve?(0,d.t)("Edit database"):(0,d.t)("Connect a database")),footer:Mt},(0,N.tZ)(Ze,null,(0,N.tZ)(me,null,(0,N.tZ)(Pe,{isLoading:xe,isEditMode:Ve,useSqlAlchemyForm:ct,hasConnectedDb:ee,db:C,dbName:ce,dbModel:ht}))),(0,N.tZ)(at,{defaultActiveKey:"1",activeKey:j,onTabClick:e=>K(e),animated:{inkBar:!0,tabPane:!0}},(0,N.tZ)(m.ZP.TabPane,{tab:(0,N.tZ)("span",null,(0,d.t)("Basic")),key:"1"},ct?(0,N.tZ)(ue,null,(0,N.tZ)(Se,{db:C,onInputChange:({target:e})=>xt(ot.inputChange,{type:e.type,name:e.name,checked:e.checked,value:e.value}),conf:Be,testConnection:()=>{var a;if(null==C||!C.sqlalchemy_uri)return void e((0,d.t)("Please enter a SQLAlchemy URI to test"));const n={sqlalchemy_uri:(null==C?void 0:C.sqlalchemy_uri)||"",database_name:(null==C||null==(a=C.database_name)?void 0:a.trim())||void 0,impersonate_user:(null==C?void 0:C.impersonate_user)||void 0,extra:null==C?void 0:C.extra,masked_encrypted_extra:(null==C?void 0:C.masked_encrypted_extra)||"",server_cert:(null==C?void 0:C.server_cert)||void 0,ssh_tunnel:(null==C?void 0:C.ssh_tunnel)||void 0,database_id:(null==C?void 0:C.id)||null};ke(!0),(0,R.xx)(n,(t=>{ke(!1),e(t)}),(e=>{ke(!1),t(e)}))},testInProgress:$e},(0,N.tZ)(He,{isEditMode:Ve,dbFetched:k,disableSSHTunnelingForEngine:et,useSSHTunneling:je,setUseSSHTunneling:Ke,setDB:S,isSSHTunneling:lt}),je&&At()),(Ot=(null==C?void 0:C.backend)||(null==C?void 0:C.engine),void 0!==(null==B||null==(qt=B.databases)||null==(Dt=qt.find((e=>e.backend===Ot||e.engine===Ot)))?void 0:Dt.parameters)&&!Ve&&(0,N.tZ)("div",{css:e=>W(e)},(0,N.tZ)(y.Z,{buttonStyle:"link",onClick:()=>S({type:ot.configMethodChange,payload:{database_name:null==C?void 0:C.database_name,configuration_method:M.DYNAMIC_FORM,engine:null==C?void 0:C.engine}}),css:e=>(e=>N.iv`
  font-weight: ${e.typography.weights.normal};
  text-transform: initial;
  padding: ${8*e.gridUnit}px 0 0;
  margin-left: 0px;
`)(e)},(0,d.t)("Connect this database using the dynamic form instead")),(0,N.tZ)(O.Z,{tooltip:(0,d.t)("Click this link to switch to an alternate form that exposes only the required fields needed to connect this database."),viewBox:"0 -6 24 24"})))):Lt(),!Ve&&(0,N.tZ)(ie,null,(0,N.tZ)(b.Z,{closable:!1,css:e=>ne(e),message:(0,d.t)("Additional fields may be required"),showIcon:!0,description:(0,N.tZ)(u.Fragment,null,(0,d.t)("Select databases require additional fields to be completed in the Advanced tab to successfully connect the database. Learn what requirements your databases has "),(0,N.tZ)("a",{href:De,target:"_blank",rel:"noopener noreferrer",className:"additional-fields-alert-description"},(0,d.t)("here")),"."),type:"info"})),pt&&Tt()),(0,N.tZ)(m.ZP.TabPane,{tab:(0,N.tZ)("span",null,(0,d.t)("Advanced")),key:"2"},(0,N.tZ)(we,{db:C,onInputChange:({target:e})=>xt(ot.inputChange,{type:e.type,name:e.name,checked:e.checked,value:e.value}),onTextChange:({target:e})=>xt(ot.textChange,{name:e.name,value:e.value}),onEditorChange:e=>xt(ot.editorChange,e),onExtraInputChange:({target:e})=>{xt(ot.extraInputChange,{type:e.type,name:e.name,checked:e.checked,value:e.value})},onExtraEditorChange:e=>{xt(ot.extraEditorChange,e)}})))):(0,N.tZ)(v.Z,{css:e=>[X,ae(e),oe(e),le(e)],name:"database",onHandledPrimaryAction:_t,onHide:gt,primaryButtonName:ee?(0,d.t)("Finish"):(0,d.t)("Connect"),width:"500px",centered:!0,show:i,title:(0,N.tZ)("h4",null,(0,d.t)("Connect a database")),footer:$t()},!xe&&ee?(0,N.tZ)(u.Fragment,null,(0,N.tZ)(Pe,{isLoading:xe,isEditMode:Ve,useSqlAlchemyForm:ct,hasConnectedDb:ee,db:C,dbName:ce,dbModel:ht,editNewDb:be}),se&&(0,N.tZ)(rt,null,(0,N.tZ)(y.Z,{buttonStyle:"secondary",onClick:()=>{var e;Ce(!0),Ce(!0),U(null==k?void 0:k.database_id).then((e=>{(0,h.LS)(h.dR.db,e)})),e=(0,p.VU)("/superset/sqllab/?db=true"),l()(s)?window.location.href=(0,p.VU)(e):null==s||s.push(e)}},(0,d.t)("QUERY DATA IN SQL LAB"))),be?Lt():(0,N.tZ)(we,{db:C,onInputChange:({target:e})=>xt(ot.inputChange,{type:e.type,name:e.name,checked:e.checked,value:e.value}),onTextChange:({target:e})=>xt(ot.textChange,{name:e.name,value:e.value}),onEditorChange:e=>xt(ot.editorChange,e),onExtraInputChange:({target:e})=>{xt(ot.extraInputChange,{type:e.type,name:e.name,checked:e.checked,value:e.value})},onExtraEditorChange:e=>xt(ot.extraEditorChange,e)})):(0,N.tZ)(u.Fragment,null,!xe&&(C?(0,N.tZ)(u.Fragment,null,(0,N.tZ)(Pe,{isLoading:xe,isEditMode:Ve,useSqlAlchemyForm:ct,hasConnectedDb:ee,db:C,dbName:ce,dbModel:ht}),dt&&(()=>{var e,t,a,n,i;const{hostname:o}=window.location;let l=(null==Je||null==(e=Je.REGIONAL_IPS)?void 0:e.default)||"";const r=(null==Je?void 0:Je.REGIONAL_IPS)||{};return Object.entries(r).forEach((([e,t])=>{const a=new RegExp(e);o.match(a)&&(l=t)})),(null==C?void 0:C.engine)&&(0,N.tZ)(ie,null,(0,N.tZ)(b.Z,{closable:!1,css:e=>ne(e),type:"info",showIcon:!0,message:(null==(t=tt[C.engine])?void 0:t.message)||(null==Je||null==(a=Je.DEFAULT)?void 0:a.message),description:(null==(n=tt[C.engine])?void 0:n.description)||(null==Je||null==(i=Je.DEFAULT)?void 0:i.description)+l}))})(),Lt(),(0,N.tZ)("div",{css:e=>W(e)},ht.engine!==I.GSheet&&(0,N.tZ)(u.Fragment,null,(0,N.tZ)(y.Z,{"data-test":"sqla-connect-btn",buttonStyle:"link",onClick:()=>S({type:ot.configMethodChange,payload:{engine:C.engine,configuration_method:M.SQLALCHEMY_URI,database_name:C.database_name}}),css:pe},(0,d.t)("Connect this database with a SQLAlchemy URI string instead")),(0,N.tZ)(O.Z,{tooltip:(0,d.t)("Click this link to switch to an alternate form that allows you to input the SQLAlchemy URL for this database manually."),viewBox:"0 -6 24 24"}))),pt&&Tt()):(0,N.tZ)(ye,null,(0,N.tZ)(Pe,{isLoading:xe,isEditMode:Ve,useSqlAlchemyForm:ct,hasConnectedDb:ee,db:C,dbName:ce,dbModel:ht}),(0,N.tZ)("div",{className:"preferred"},null==B||null==(It=B.databases)?void 0:It.filter((e=>e.preferred)).map((e=>(0,N.tZ)(L,{className:"preferred-item",onClick:()=>wt(e.name),buttonText:e.name,icon:null==Qe?void 0:Qe[e.engine],key:`${e.name}`})))),(()=>{var e,t;return(0,N.tZ)("div",{className:"available"},(0,N.tZ)("h4",{className:"available-label"},(0,d.t)("Or choose from a list of other databases we support:")),(0,N.tZ)("div",{className:"control-label"},(0,d.t)("Supported databases")),(0,N.tZ)(g.IZ,{className:"available-select",onChange:wt,placeholder:(0,d.t)("Choose a database..."),showSearch:!0},null==(e=[...(null==B?void 0:B.databases)||[]])?void 0:e.sort(((e,t)=>e.name.localeCompare(t.name))).map((e=>(0,N.tZ)(g.IZ.Option,{value:e.name,key:e.name},e.name))),(0,N.tZ)(g.IZ.Option,{value:"Other",key:"Other"},(0,d.t)("Other"))),(0,N.tZ)(b.Z,{showIcon:!0,closable:!1,css:e=>ne(e),type:"info",message:(null==Je||null==(t=Je.ADD_DATABASE)?void 0:t.message)||(0,d.t)("Want to add a new database?"),description:null!=Je&&Je.ADD_DATABASE?(0,N.tZ)(u.Fragment,null,(0,d.t)("Any databases that allow connections via SQL Alchemy URIs can be added. "),(0,N.tZ)("a",{href:null==Je?void 0:Je.ADD_DATABASE.contact_link,target:"_blank",rel:"noopener noreferrer"},null==Je?void 0:Je.ADD_DATABASE.contact_description_link)," ",null==Je?void 0:Je.ADD_DATABASE.description):(0,N.tZ)(u.Fragment,null,(0,d.t)("Any databases that allow connections via SQL Alchemy URIs can be added. Learn about how to connect a database driver "),(0,N.tZ)("a",{href:De,target:"_blank",rel:"noopener noreferrer"},(0,d.t)("here")),".")}))})(),(0,N.tZ)(_e,null,(0,N.tZ)(g.gq,{name:"databaseFile",id:"databaseFile","data-test":"database-file-input",accept:".yaml,.json,.yml,.zip",customRequest:()=>{},onChange:async e=>{if(Fe(""),ze([]),Ee({}),Ie(!0),Le([{...e.file,status:"done"}]),!(e.file.originFileObj instanceof File))return;await Zt(e.file.originFileObj,Ne,Ue)&&(null==a||a(1))},onRemove:e=>(Le(Ae.filter((t=>t.uid!==e.uid))),!1)},(0,N.tZ)(y.Z,{"data-test":"import-database-btn",buttonStyle:"link",type:"link",css:he},(0,d.t)("Import database from file")))),Nt()))),xe&&(0,N.tZ)(H.Z,null));var It,Ot,qt,Dt}))},301483:(e,t,a)=>{"use strict";a.d(t,{c:()=>i});var n=a(828216);function i(){return(0,n.v9)((e=>{var t;return null==e||null==(t=e.common)?void 0:t.conf}))}},977230:(e,t,a)=>{"use strict";a.d(t,{Z:()=>ie});var n=a(205872),i=a.n(n),o=a(23279),l=a.n(o),r=a(667294),s=a(751995),d=a(211965),c=a(667496),u=a(23525),p=a(49937),h=a(683862),m=a(358593),g=a(473727),b=a(685931),v=a(731293),y=a(229147),f=a(427600),Z=a(441609),x=a.n(Z),_=a(115926),w=a.n(_),C=a(828216),S=a(535755),$=a(97849),k=a(175049),N=a(455867),E=a(431069),U=a(737921),T=a(212617),A=a(653002);const{SubMenu:L}=h.$t,M=s.iK.div`
  display: flex;
  align-items: center;

  & i {
    margin-right: ${({theme:e})=>2*e.gridUnit}px;
  }

  & a {
    display: block;
    width: 150px;
    word-wrap: break-word;
    text-decoration: none;
  }
`,I=s.iK.i`
  margin-top: 2px;
`;function O(e){const{locale:t,languages:a,...n}=e;return(0,d.tZ)(L,i()({"aria-label":"Languages",title:(0,d.tZ)("div",{className:"f16"},(0,d.tZ)(I,{className:`flag ${a[t].flag}`})),icon:(0,d.tZ)(v.Z.TriangleDown,null)},n),Object.keys(a).map((e=>(0,d.tZ)(h.$t.Item,{key:e,style:{whiteSpace:"normal",height:"auto"}},(0,d.tZ)(M,{className:"f16"},(0,d.tZ)("i",{className:`flag ${a[e].flag}`}),(0,d.tZ)("a",{href:(0,c.VU)(a[e].url)},a[e].name))))))}var q,D=a(806646),F=a(440768);!function(e){e.GOOGLE_SHEETS="gsheets",e.DB_CONNECTION="dbconnection",e.DATASET_CREATION="datasetCreation"}(q||(q={}));const P=(0,k.I)(),R=e=>d.iv`
  padding: ${1.5*e.gridUnit}px ${4*e.gridUnit}px
    ${4*e.gridUnit}px ${7*e.gridUnit}px;
  color: ${e.colors.grayscale.base};
  font-size: ${e.typography.sizes.xs}px;
  white-space: nowrap;
`,z=s.iK.div`
  display: flex;
  flex-direction: row;
  justify-content: ${({align:e})=>e};
  align-items: center;
  margin-right: ${({theme:e})=>e.gridUnit}px;
  .ant-menu-submenu-title > svg {
    top: ${({theme:e})=>5.25*e.gridUnit}px;
  }
`,H=s.iK.div`
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
`,j=s.iK.a`
  padding-right: ${({theme:e})=>e.gridUnit}px;
  padding-left: ${({theme:e})=>e.gridUnit}px;
`,K=e=>d.iv`
  color: ${e.colors.grayscale.light5};
`,{SubMenu:B}=h.$t;var Q={name:"1bmnxg7",styles:"white-space:nowrap"};const J=({align:e,settings:t,navbarRight:a,isFrontendRoute:n,environmentTag:i,setQuery:o})=>{const l=(0,C.v9)((e=>e.user)),c=(0,C.v9)((e=>{var t;return null==(t=e.dashboardInfo)?void 0:t.id})),u=l||{},{roles:p}=u,{CSV_EXTENSIONS:m,COLUMNAR_EXTENSIONS:b,EXCEL_EXTENSIONS:y,ALLOWED_EXTENSIONS:f}=(0,C.v9)((e=>e.common.conf)),[Z,_]=(0,r.useState)(!1),[S,k]=(0,r.useState)(""),L=(0,T.R)("can_write","Database",p),M=(0,T.R)("can_write","Dataset",p),{canUploadData:I,canUploadCSV:J,canUploadColumnar:V,canUploadExcel:G}=(0,F.Mc)(p,m,b,y,f),[Y,X]=(0,r.useState)(!1),[W,ee]=(0,r.useState)(!1),te=(0,A.i5)(l),ae=Y||te,ne=[{label:(0,N.t)("Data"),icon:"fa-fw fa-database",childs:[{label:(0,N.t)("Connect database"),name:q.DB_CONNECTION,perm:L&&!W},{label:(0,N.t)("Create dataset"),name:q.DATASET_CREATION,url:"/dataset/add/",perm:M&&W},{label:(0,N.t)("Upload CSV to database"),name:"Upload a CSV",url:"/csvtodatabaseview/form",perm:J&&ae,disable:te&&!Y},{label:(0,N.t)("Upload columnar file to database"),name:"Upload a Columnar file",url:"/columnartodatabaseview/form",perm:V&&ae,disable:te&&!Y},{label:(0,N.t)("Upload Excel file to database"),name:"Upload Excel",url:"/exceltodatabaseview/form",perm:G&&ae,disable:te&&!Y}]},{label:(0,N.t)("SQL query"),url:"/superset/sqllab?new=true",icon:"fa-fw fa-search",perm:"can_sqllab",view:"Superset"},{label:(0,N.t)("Chart"),url:Number.isInteger(c)?`/chart/add?dashboard_id=${c}`:"/chart/add",icon:"fa-fw fa-bar-chart",perm:"can_write",view:"Chart"},{label:(0,N.t)("Dashboard"),url:"/dashboard/new",icon:"fa-fw fa-dashboard",perm:"can_write",view:"Dashboard"}],ie=()=>{E.Z.get({endpoint:`/api/v1/database/?q=${w().encode({filters:[{col:"allow_file_upload",opr:"upload_is_enabled",value:!0}]})}`}).then((({json:e})=>{var t;const a=(null==e||null==(t=e.result)?void 0:t.filter((e=>{var t;return null==e||null==(t=e.engine_information)?void 0:t.supports_file_upload})))||[];X((null==a?void 0:a.length)>=1)}))},oe=()=>{E.Z.get({endpoint:`/api/v1/database/?q=${w().encode({filters:[{col:"database_name",opr:"neq",value:"examples"}]})}`}).then((({json:e})=>{ee(e.count>=1)}))};(0,r.useEffect)((()=>{I&&ie()}),[I]),(0,r.useEffect)((()=>{(L||M)&&oe()}),[L,M]);const le=P.get("navbar.right"),re=P.get("navbar.right-menu.item.icon"),se=(0,s.Fg)();return(0,d.tZ)(z,{align:e},L&&(0,d.tZ)(D.ZP,{onHide:()=>{k(""),_(!1)},show:Z,dbEngine:S,onDatabaseAdd:()=>o({databaseAdded:!0})}),(null==i?void 0:i.text)&&(0,d.tZ)(U.Z,{css:(0,d.iv)({borderRadius:125*se.gridUnit+"px"},"",""),color:/^#(?:[0-9a-f]{3}){1,2}$/i.test(i.color)?i.color:i.color.split(".").reduce(((e,t)=>e[t]),se.colors)},(0,d.tZ)("span",{css:K},i.text)),(0,d.tZ)(h.$t,{selectable:!1,mode:"horizontal",onClick:e=>{e.key===q.DB_CONNECTION?_(!0):e.key===q.GOOGLE_SHEETS&&(_(!0),k("Google Sheets"))},onOpenChange:e=>(e.length>1&&!x()(null==e?void 0:e.filter((e=>{var t;return e.includes(`sub2_${null==ne||null==(t=ne[0])?void 0:t.label}`)})))&&(I&&ie(),(L||M)&&oe()),null)},le&&(0,d.tZ)(le,null),(0,d.tZ)(B,{title:(0,N.t)("Settings"),icon:(0,d.tZ)(v.Z.TriangleDown,{iconSize:"xl"})},null==t||null==t.map?void 0:t.map(((e,a)=>{var i;return[(0,d.tZ)(h.$t.ItemGroup,{key:`${e.label}`,title:e.label},null==e||null==(i=e.childs)||null==i.map?void 0:i.map((e=>{if("string"!==typeof e){const t=re?(0,d.tZ)(H,null,e.label,(0,d.tZ)(re,{menuChild:e})):e.label;return"/logmodelview/list/"==e.url&&(e.url="/sys/logs/"),(0,d.tZ)(h.$t.Item,{key:`${e.label}`},n(e.url)?(0,d.tZ)(g.rU,{to:e.url||""},t):(0,d.tZ)("a",{href:e.url},t))}return null}))),a<t.length-1&&(0,d.tZ)(h.$t.Divider,{key:`divider_${a}`})]})),!a.user_is_anonymous&&[(0,d.tZ)(h.$t.Divider,{key:"user-divider"}),(0,d.tZ)(h.$t.ItemGroup,{key:"user-section",title:(0,N.t)("User")},a.user_profile_url&&(0,d.tZ)(h.$t.Item,{key:"profile"},(0,d.tZ)("a",{href:a.user_profile_url},(0,N.t)("Profile"))),(null==l?void 0:l.isAdmin)&&a.user_info_url&&(0,d.tZ)(h.$t.Item,{key:"info"},(0,d.tZ)("a",{href:a.user_info_url},(0,N.t)("Info"))),(0,d.tZ)(h.$t.Item,{key:"logout",onClick:()=>{(0,$.oD)()}},(0,d.tZ)("a",{href:a.user_logout_url},(0,N.t)("Logout"))))],(a.version_string||a.version_sha)&&[(0,d.tZ)(h.$t.Divider,{key:"version-info-divider"}),(0,d.tZ)(h.$t.ItemGroup,{key:"about-section",title:(0,N.t)("About")},(0,d.tZ)("div",{className:"about-section"},a.show_watermark&&(0,d.tZ)("div",{css:R},(0,N.t)("Powered by Apache Superset")),a.version_string&&(0,d.tZ)("div",{css:R},(0,N.t)("Version"),": ",a.version_string),a.version_sha&&(0,d.tZ)("div",{css:R},(0,N.t)("SHA"),": ",a.version_sha),a.build_number&&(0,d.tZ)("div",{css:R},(0,N.t)("Build"),": ",a.build_number)))]),a.show_language_picker&&(0,d.tZ)(O,{locale:a.locale,languages:a.languages})),a.documentation_url&&(0,d.tZ)(r.Fragment,null,(0,d.tZ)(j,{href:a.documentation_url,target:"_blank",rel:"noreferrer",title:a.documentation_text||(0,N.t)("Documentation"),css:Q},(0,N.t)("Documentation Text"),(0,d.tZ)("span",null,"\xa0"),a.documentation_icon?(0,d.tZ)("i",{className:a.documentation_icon}):(0,d.tZ)("i",{className:"fa fa-question"})),(0,d.tZ)("span",null,"\xa0")),a.bug_report_url&&(0,d.tZ)(r.Fragment,null,(0,d.tZ)(j,{href:a.bug_report_url,target:"_blank",rel:"noreferrer",title:a.bug_report_text||(0,N.t)("Report a bug")},a.bug_report_icon?(0,d.tZ)("i",{className:a.bug_report_icon}):(0,d.tZ)("i",{className:"fa fa-bug"})),(0,d.tZ)("span",null,"\xa0")),a.user_is_anonymous&&(0,d.tZ)(j,{href:a.user_login_url},(0,d.tZ)("i",{className:"fa fa-fw fa-sign-in"}),(0,N.t)("Login")))},V=e=>{const[,t]=(0,S.Kx)({databaseAdded:S.dJ,datasetAdded:S.dJ});return(0,d.tZ)(J,i()({setQuery:t},e))};class G extends r.PureComponent{constructor(...e){super(...e),this.state={hasError:!1},this.noop=()=>{}}static getDerivedStateFromError(){return{hasError:!0}}render(){return this.state.hasError?(0,d.tZ)(J,i()({setQuery:this.noop},this.props)):this.props.children}}const Y=e=>(0,d.tZ)(G,e,(0,d.tZ)(V,e));var X=a(454076);const W=s.iK.header`
  ${({theme:e})=>d.iv`
    height: ${e.navMenuHeight}px;
    background-color: ${e.colors.main.base};
    margin-bottom: 2px;
    z-index: 10;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;

    &:nth-last-of-type(2) nav {
      margin-bottom: 2px;
    }
    .caret {
      display: none;
    }
    .navbar-brand {
      display: flex;
      flex-direction: column;
      justify-content: center;
      /* must be exactly the height of the Antd navbar */
      min-height: ${e.navMenuHeight}px;
      padding: ${e.gridUnit}px ${2*e.gridUnit}px ${e.gridUnit}px
        ${4*e.gridUnit}px;
      width: ${e.sideMenuWidth}px;
      img {
        height: 100%;
        object-fit: contain;
        flex-shrink: 0;
      }
    }
    .navbar-brand-text {
      border-left: 1px solid ${e.colors.grayscale.light2};
      border-right: 1px solid ${e.colors.grayscale.light2};
      height: 100%;
      color: ${e.colors.grayscale.dark1};
      padding-left: ${4*e.gridUnit}px;
      padding-right: ${4*e.gridUnit}px;
      margin-right: ${6*e.gridUnit}px;
      font-size: ${4*e.gridUnit}px;
      float: left;
      display: flex;
      flex-direction: column;
      justify-content: center;

      span {
        max-width: ${58*e.gridUnit}px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
      }
      @media (max-width: 1127px) {
        display: none;
      }
    }
    .main-nav {
      display: flex;
    }
    .main-nav .ant-menu-submenu-title > svg {
      top: ${5.25*e.gridUnit}px;
    }
    .ant-menu {
      background-color: ${e.colors.main.base};
    }
    .ant-menu-horizontal .ant-menu-item {
      height: 100%;
      line-height: inherit;
    }
    .ant-menu > .ant-menu-item > a {
      padding: ${4*e.gridUnit}px;
    }
    @media (max-width: 767px) {
      .ant-menu-item {
        padding: 0 ${6*e.gridUnit}px 0 ${3*e.gridUnit}px !important;
      }
      .ant-menu > .ant-menu-item > a {
        padding: 0px;
      }
      .main-nav .ant-menu-submenu-title > svg:nth-of-type(1) {
        display: none;
      }
      .ant-menu-item-active > a {
        &:hover {
          color: #5d9cec !important;
          background-color: #5d9cec !important;
        }
      }
    }
    .ant-menu-item a,
    .ant-menu-submenu {
      &:hover {
        color: ${e.colors.grayscale.dark1};
        background-color: ${e.colors.primary.light5};
        border-bottom: none;
        margin: 0;
        &:after {
          opacity: 1;
          width: 100%;
        }
      }
    }
  `}
`,ee=e=>d.iv`
  .ant-menu-submenu.ant-menu-submenu-popup.ant-menu.ant-menu-light.ant-menu-submenu-placement-bottomLeft {
    border-radius: 0px;
  }
  .ant-menu-submenu.ant-menu-submenu-popup.ant-menu.ant-menu-light {
    border-radius: 0px;
  }
  .ant-menu-vertical > .ant-menu-submenu.data-menu > .ant-menu-submenu-title {
    i:not(.ant-menu-submenu-arrow) {
      padding-right: ${2*e.gridUnit}px;
      margin-left: ${1.75*e.gridUnit}px;
    }
  }
`,{SubMenu:te}=h.$t,{useBreakpoint:ae}=p.rj;function ne({data:{menu:e,brand:t,navbar_right:a,settings:n,environment_tag:i},isFrontendRoute:o=(()=>!1)}){const[Z,x]=(0,r.useState)(-1),_=ae(),w=(0,y.fG)(),C=(0,s.Fg)();(0,r.useEffect)((()=>{function e(){x(window.innerWidth)}e();const t=l()((()=>e()),100);return window.addEventListener("resize",t),()=>window.removeEventListener("resize",t)}),[]);const S=(0,u.eY)(f.KD.standalone);if((0,X.w)())return(0,d.tZ)(r.Fragment,null);if(S||w.hideNav)return(0,d.tZ)(r.Fragment,null);const $=({label:e,childs:t,url:a,index:n,isFrontendRoute:i})=>a&&i?(0,d.tZ)(h.$t.Item,{key:e,role:"presentation"},(0,d.tZ)(g.rU,{role:"button",to:(0,c.Rs)(a),onClick:()=>(e=>{window.location.pathname!==e&&(sessionStorage.removeItem("key"),sessionStorage.removeItem("keyPath"),sessionStorage.removeItem("chartIds"),sessionStorage.removeItem("chartTitle"),sessionStorage.removeItem("chart_basicInfo"))})(a)},e)):a?(0,d.tZ)(h.$t.Item,{key:e},(0,d.tZ)("a",{href:(0,c.VU)(a)},e)):(0,d.tZ)(te,{key:n,title:e,icon:(0,d.tZ)(v.Z.TriangleDown,null)},null==t?void 0:t.map(((t,a)=>"string"===typeof t&&"-"===t&&"Data"!==e?(0,d.tZ)(h.$t.Divider,{key:`$${a}`}):"string"!==typeof t?(0,d.tZ)(h.$t.Item,{key:`${t.label}`},t.isFrontendRoute?(0,d.tZ)(g.rU,{to:(0,c.Rs)(t.url||"")},t.label):(0,d.tZ)("a",{href:(0,c.VU)(t.url)},t.label)):null)));return(0,d.tZ)(W,{className:"top",id:"main-menu",role:"navigation"},(0,d.tZ)(d.xB,{styles:ee(C)}),(0,d.tZ)(p.X2,null,(0,d.tZ)(p.JX,{span:16},(0,d.tZ)(m.u,{id:"brand-tooltip",placement:"bottomLeft",title:t.tooltip,arrowPointAtCenter:!0},o(window.location.pathname)?(0,d.tZ)(b.m,{className:"navbar-brand",to:(0,c.Rs)(t.path)},(0,d.tZ)("img",{src:t.icon,alt:t.alt})):(0,d.tZ)("a",{className:"navbar-brand",href:(0,c.VU)(t.path)},(0,d.tZ)("img",{src:t.icon,alt:t.alt}))),t.text&&(0,d.tZ)("div",{className:"navbar-brand-text"},(0,d.tZ)("span",null,t.text)),(0,d.tZ)(h.$t,{mode:"horizontal","data-test":"navbar-top",className:"main-nav"},e.map(((e,t)=>{var a;const n={index:t,...e,isFrontendRoute:o(e.url),childs:null==(a=e.childs)?void 0:a.map((e=>"string"===typeof e?e:{...e,isFrontendRoute:o(e.url)}))};return $(n)})))),(0,d.tZ)(p.JX,{span:8},(0,d.tZ)(Y,{key:`right-menu-${String(Z)}`,align:_.md?"flex-end":"flex-start",settings:n,navbarRight:a,isFrontendRoute:o,environmentTag:i}))))}function ie({data:e,...t}){const a={...e},n={Security:!0,Manage:!0,Data:!0,Records:!0},o=[],l=[];return a.menu.forEach((e=>{if(!e)return;const t=[],a={...e};e.childs&&(e.childs.forEach((e=>{("string"===typeof e||e.label)&&t.push(e)})),a.childs=t),n.hasOwnProperty(e.name)?l.push(a):o.push(a)})),a.menu=o,a.settings=l,(0,d.tZ)(ne,i()({data:a},t))}}}]);
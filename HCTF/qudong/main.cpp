#include <iostream>
#include <tchar.h>
#include <Windows.h>
#include "InputBuffer.h"
using std::cout;
using std::endl;

int _tmain(int argc, _TCHAR* argv[])
{
    /************************************����˵��*********************************************
    * ��������CreateFile                                                                     *
    * ���ͣ�Win32 API����                                                                    *
    * ���ã�����һ�๦�ܵĺ������ɴ򿪻򴴽��磺����̨��ͨ����Դ��Ŀ¼��ֻ���򿪣���                    *
    * �������������ļ����ʲۣ��ܵ��ȶ��󣬲����ؿɷ��ʵľ������                                     *
    * ����˵����                                                                             *
    * LPCTSTR lpFileName �� ��ͨ�ļ��������豸�ļ���                                            *
    * DWORD dwDesiredAccess �� ���ʶ����Ȩ�ޣ�ϣ�������ַ�ʽ��,�������߼汸��                    *
    * DWORD dwShareMode �� ����ģʽ���������߼汸��                                             *
    * LPSECURITY_ATTRIBUTES �� �����趨һ��ָ���Ƿ����ӽ��̷��صľ�����Ա��̳�                     *
    * DWORD dwCreationDisposition �� ��ʾ�ж��ļ����ڻ򲻴��ڣ���������δ���                      *
    * DWORD dwFlagsAndAttributes �� �ļ���־���豸����                                         *
    * HANDLE hTemplateFile ��ģ���ļ�,���������ļ��ṩ�ļ����Ժ���չ���ԣ�һ��Ϊ��                   *
    * ����ֵ�� ��ȡ�豸�ľ��                                                                   *
    *****************************************************************************************/
    HANDLE  DeviceHandle = CreateFile(
        L"\\\\.\\AppSymbolLink",              //\\??\\�豸������������,ע������Ҫ�� L ���ַ�ת��
        GENERIC_READ | GENERIC_WRITE,
        FILE_SHARE_READ | FILE_SHARE_WRITE,
        NULL,
        OPEN_EXISTING,                        //ö�٣�OPEN_EXISTING ��ʾ�ļ������Ѿ����ڡ�
        FILE_ATTRIBUTE_NORMAL,                 //��ö�ٱ�ʾ�ļ�û���������Լ���
        NULL);                                 //ģ���ļ�,һ��Ϊ��
    if (DeviceHandle == INVALID_HANDLE_VALUE){
        printf("��ȡ�ļ����豸���ʧ�ܣ���");
        getchar();                            //��ȡ����������ַ�
        return -1;
    }

        printf("��ȡ�����������ɹ� \n");
        int a=10, b=20, c=30,e=0,f=0,g=0;
        InputBuffer(DeviceHandle, a, b, c);
        for (int i = 0; i < 3; i++)
        {
            switch (i){
            case 0:{
                       e = OtnC[i];
            }
            case 1:{
                       f = OtnC[i];
            }
            case 2:{
                       g = OtnC[i];
            }
            } //End switch (i)
        }  //End for

    printf("a=%d,b=%d,c=%d\n",e, f, g);
    CloseHandle(DeviceHandle);            //������ɺ���ùرվ��
    cout << "����ͨѶ���" << endl;
    system("pause");
}
